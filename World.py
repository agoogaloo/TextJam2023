path = "levels/level"
world = []
file = open(path, "r")
world = file.readlines()

x = 0
y = 0
for i in range(len(world)):
    world[i] = world[i].replace("W", " H")
    world[i] = world[i].replace("\n", "")
    world[i] = world[i].replace(" ", "  ")
    