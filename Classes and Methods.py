# %%
# Essentially, Python is an object oriented programming language. Hence, everything in Python is pretty much an object
# with it's own methods.
# First some definitions.
# An object is simply a collection of data (variables) and methods (functions) that act on said data.
# A class is essentially a blueprint for said object.
# Let's make a simple class to start with.
class Bandit:
    health = 5
    stamina = 3
    
    def attack(self):
        print("Skyrim belongs to the Nords!")
        self.stamina -= 1
        
    def defend(self):
        print("Mercy! I yield!")
        self.stamina += 1
        if(self.health < 5):
            self.health += 1
        
# The reason we pass the "self" parameter in the internal function is because it represents the instance of the class.
# With that, you can access the class itself. You don't have to use self if you don't want to. You can use some other
# word but its just the common way that everyone does it.

# Now let's use this class and show it off.
john = Bandit()                                         # Create an object based on our Bandit class
john.attack()                                           # Have our "bandit" attack something
print("John's stamina is " + str(john.stamina))         # Show off the stamina of our bandit
john.defend()                                           # Have our "bandit" defend
print("John's stamina is " + str(john.stamina))         # Show off the stamina of our bandit
print("John's health is " + str(john.health))           # Show off the health of our bandit
# We can see that the attack and defend functions are the methods of the Bandit class. By calling the method
# through our created object, we can use the functions within our created class.
# %%

# %%
# Now what if we want to define how much health and stamina our Bandit has at initialization?
# Let's reconfigure our class to take that into account.
class Bandit:
    def __init__(self, health, stamina):
        self.health = health
        self.stamina = stamina
    
    def attack(self):
        print("Skyrim belongs to the Nords!")
        self.stamina -= 1
        
    def defend(self):
        print("Mercy! I yield!")
        self.stamina += 1
        if(self.health < 5):
            self.health += 1
        
john = Bandit(10,5)                                     # Create an object based on our Bandit class. We will also give a custom health and stamina level
carl = Bandit(5,3)                                      # Create a second "bandit" with different health and stamina
print("John will begin to move.")
john.attack()                                           # Have our "bandit" attack something
print("John's stamina is " + str(john.stamina))         # Show off the stamina of our bandit
john.defend()                                           # Have our "bandit" defend
print("John's stamina is " + str(john.stamina))         # Show off the stamina of our bandit
print("John's health is " + str(john.health))           # Show off the health of our bandit
print("Carl will begin to move.")                       # Have our second bandit do stuff
carl.attack()
print("Carl's stamina is " + str(carl.stamina))
carl.defend()
print("Carl's stamina is " + str(carl.stamina))
print("Carl's health is " + str(carl.health))
# %%

'''
You can continue to add on and tinker with this class if you would like. You can try to pass an argument through
attack() in the class definition so you can maybe change what the voice line will be or how much stamina is lost.
Its your class so you get creative with it if you like.
'''