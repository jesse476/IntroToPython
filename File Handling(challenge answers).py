# Now let's do some challenges to test your comprehension.
# %%
# Challenge 1: Write a file that has a list of your top 3 favorite movie lines. Check the file to see if it worked.
with open("challenge1.txt", "w") as f:
    f.write("1. Hasta la vista, baby.\n")
    f.write("2. The arrogance of man is thinking nature is in our control, and not the other way around. Let them fight.\n")
    f.write("3. Come on you apes! You want to live forever?\n")
with open("challenge1.txt") as f:
    print(f.read())
# %%

# %%
# Challenge 2: Combine two lines from two separate files and print them.
with open("challenge2.txt", "w") as f:
    g = open("demofile.txt")
    h = open("challenge1.txt")
    line1 = g.readline()
    line2 = h.readline()
    f.write(line1 + "\n" + line2)
    g.close()
    h.close()

with open("challenge2.txt") as f:
    print(f.read())
# %%