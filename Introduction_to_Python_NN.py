# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:24:43 2020

@author: jonathan
"""

# import numpy as np
import pandas as pd

# load data & remove missing
dataset = pd.read_csv('SDGE_Time_Series_Data.csv') 
removed_missing_data = dataset.dropna() # leaves us with 2017-2019 data
dataset = removed_missing_data

# manually specify column names
dataset = dataset.rename(
    {'Date_Hour':'Datetime',
     'Average of HourlyDryBulbTemperature':'DBT',
     'Average of HourlyRelativeHumidity':'RH',
     'Average of THI':'THI',
     'Average of Load':'Load_MW'},
    axis = 'columns')

# reorganize columns to have the following format:
# Column 1: Index (e.g., datetime for hourly data/predictions or date for daily data/predictions)
# Column 2: Variable we want to predict
# Columns 3+: [numeric features] [categorical features] ]
    # interchangeable terminology: features <=> predictors <=> columns
dataset = dataset[['Datetime','Load_MW','DBT','RH','THI']]

# Create the necessary columns for analysis at various timescales
dataset['Datetime'] = pd.to_datetime(dataset['Datetime'])
'''
dataset['Year'] = dataset['Datetime'].dt.year
dataset['Quarter'] = dataset['Datetime'].dt.quarter
dataset['Month'] = pd.DatetimeIndex(dataset['Datetime']).month
dataset['Day'] = pd.DatetimeIndex(dataset['Datetime']).day
dataset['Hour'] = pd.to_datetime(dataset['Datetime']).dt.hour
'''
# Setup Index
dataset.index = dataset['Datetime']
dataset.index.name = 'date'
dataset.drop('Datetime', axis=1, inplace=True)

# summarize first 5 rows
print(dataset.head(-5))

# save to file
dataset.to_csv('prepped_dataset.csv')

#%%

from pandas import read_csv
from matplotlib import pyplot

# load dataset
dataset = read_csv('prepped_dataset.csv', header=0, index_col=0)
values = dataset.values
# specify columns to plot
groups = [0, 1, 2, 3]
i = 1
# plot each column
pyplot.figure(num=None, figsize=(20, 10), dpi=80, facecolor='w', edgecolor='k')
for group in groups:
    pyplot.subplot(len(groups),1, i)
    pyplot.plot(values[:, group])
    pyplot.title(dataset.columns[group], y=0.5, loc='right')
    i += 1
pyplot.subplots_adjust(hspace=0.125)
pyplot.show()
#%%

# prepare data for lstm
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
 
# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    """
	Frame a time series as a supervised learning dataset.
	Arguments:
		data: Sequence of observations as a list or NumPy array.
		n_in: Number of lag observations as input (X).
		n_out: Number of observations as output (y).
		dropnan: Boolean whether or not to drop rows with NaN values.
	Returns:
		Pandas DataFrame of series framed for supervised learning.
    
    Notes on shift(): 
        shift() will shift values backward (values in column move 
    downward if first entry is first time step) to get values prior
    to the current time step as input as predictors.
        shift() will shift values forward (values in column move 
    down if first entry is first time step) to get values after
    the current time step as output to check against.
	"""
    
    #define number of variables AKA features or columns
        #data.shape returns (numRows,numCols) so data.shape[1]
        #returns the number of columns (variables)
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg
 
# load dataset
dataset = read_csv('prepped_dataset.csv', header=0, index_col=0)
values = dataset.values
# ensure all data is float
values = values.astype('float32')
# normalize features (columns)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
# frame as supervised learning
n_in = 1 #1 timesteps as input (1 hour and two hours prior to current time step)
n_out = 1 # 1 timestep as output  (current time step)
reframed = series_to_supervised(scaled, n_in, n_out)

# drop columns we don't want to predict
print(scaled.shape[1])
columns_to_drop = range(n_in*scaled.shape[1]+1,(n_in+n_out)*scaled.shape[1],1)
print(columns_to_drop)
reframed.drop(reframed.columns[columns_to_drop], axis=1, inplace=True)
print("reframed.head() output:\n")
print(reframed.head())
#'''

#%%

# split into train and test sets
values = reframed.values
n_train_hours = 2 * 365 * 24 # (2 years of data out of 3 total)
train = values[:n_train_hours, :] # selects the first n_train_hours for all columns
test = values[n_train_hours:, :] # selects all hours after the first n_train_hours for all columns
# split into input and outputs
 # the variable we want to predict is the last column,
 # so we ommit it from inputs X and use it to define the output y.
 # X is capitalized; it represents the matrix of input vectors (each row is an input vector).
 # y is lower case; it represents a column vector of output values (each row/element is the
 # value we want the neural network to compare its results with to improve its accuracy during
 # the training phase, and it is the value we want the neural network to be able to predict
 # for the test phase.
 # As such, you will see in the next section that we want to have input neurals equal to the number
 # of features (4) and output neurons equal to the number of outputs (1)
train_X, train_y = train[:, :-1], train[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]
# reshape input to be 3D [samples, timesteps, features]
 # samples = rows or .shap[0]
 # features = columns or .shape[1]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)
print(train_X.shape[1])
print(train_X.shape[2])

#%%

from keras.models import Sequential
from matplotlib import pyplot
from keras.layers import LSTM
from keras.layers import Dense

# design network
model = Sequential()
# 50 neurons in the first hidden layer
# input is 1 time step with 4 features (4 neurons)
 # Remember, the data is in 3D form. 
 # X.shape[1] = single timestep (1), X.shape[2] = number features (4)
 # Thus each input X is a column vector.
# 1 neuron in the output layer
 # Thus each output y is a scalar.
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
# fit network
 # Epoch: One pass through all samples in the training dataset and updating the network weights. LSTMs may be trained for tens, hundreds, or thousands of epochs.
 # Batch: A pass through a subset of samples in the training dataset after which the network weights are updated. One epoch is comprised of one or more batches.
  # The batch size is the number of samples between updates to the model weights. A good default batch size is 32 samples.
  # In this case, we have a batch size of 72.
history = model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2, shuffle=False)
# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()

#%%

from math import sqrt
from numpy import concatenate
from sklearn.metrics import mean_squared_error

# make a prediction
yhat = model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
# invert scaling for forecast
inv_yhat = concatenate((yhat, test_X[:, 1:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:,0]
# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = concatenate((test_y, test_X[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:,0]
# calculate RMSE
rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
print('Test RMSE: %.3f' % rmse)



#%%



# MULTIPLE INPUT TIMESTEPS (n_in > 1)
from pandas import read_csv
from matplotlib import pyplot

# load dataset
dataset = read_csv('prepped_dataset.csv', header=0, index_col=0)
values = dataset.values
# ensure all data is float
values = values.astype('float32')
# normalize features (columns)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
# frame as supervised learning
n_in = 3 #3 timesteps as input (1 hour, two hours, and three prior to current time step)
n_out = 1 # 1 timestep as output  (current time step)
n_features = 4
n_observations = n_in * n_features
reframed = series_to_supervised(scaled, n_in, n_out)

#%%

# split into train and test sets
values = reframed.values
n_train_hours = 2 * 365 * 24 # (2 years of data out of 3 total)
train = values[:n_train_hours, :] # selects the first n_train_hours for all columns
test = values[n_train_hours:, :] # selects all hours after the first n_train_hours for all columns
# split into input and outputs
 # for inputs, X
    # [:,:n_obs] --> all rows,
    #first n_observations columns
 # for outputs, y
    # [:,:-n_features] --> all rows,
    # last ((n_observations + n_features) - 1 + (-n_features) = n_observations-1
    # Index starts at 0, so data[n_observations-1] is var1(t); the output value we wish to predict
 # Overall, this is a more efficient way to do what we did previously
train_X, train_y = train[:, :n_observations], train[:, -n_features]
test_X, test_y = test[:, :n_observations], test[:, -n_features]
print(train_X.shape, len(train_X), train_y.shape)

# reshape input to be 3D [samples, timesteps, features]
 # samples = rows or .shap[0]
 # features = columns or .shape[1]
 # We stick with n_featuers, rather than n_observations because the LSTM remembers
 # values from up to 3 hours prior to the current timestep; we created more columns,
 # but they are for the same feature!
train_X = train_X.reshape((train_X.shape[0], n_in, n_features))
test_X = test_X.reshape((test_X.shape[0], n_in, n_features))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)

#%%

from keras.models import Sequential
from matplotlib import pyplot
from keras.layers import LSTM
from keras.layers import Dense

# design network
model = Sequential()
# 50 neurons in the first hidden layer
# input is 1 time step with 4 features (4 neurons)
 # Remember, the data is in 3D form.
 # X.shape[1] = single timestep (1), X.shape[2] = number features (4)
 # Thus each input X is a column vector.
# 1 neuron in the output layer
 # Thus each output y is a scalar.
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
# fit network
 # Epoch: One pass through all samples in the training dataset and updating the network weights. LSTMs may be trained for tens, hundreds, or thousands of epochs.
 # Batch: A pass through a subset of samples in the training dataset after which the network weights are updated. One epoch is comprised of one or more batches.
  # The batch size is the number of samples between updates to the model weights. A good default batch size is 32 samples.
  # In this case, we have a batch size of 72.
history = model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2, shuffle=False)
# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()

#%%

from math import sqrt
from numpy import concatenate
from sklearn.metrics import mean_squared_error

# make a prediction
yhat = model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], n_observations))
# invert scaling for forecast
inv_yhat = concatenate((yhat, test_X[:, -(n_features-1):]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:,0]
# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = concatenate((test_y, test_X[:, -(n_features-1):]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:,0]
# calculate RMSE
rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
print('Test RMSE: %.3f' % rmse)
