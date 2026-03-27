f = open("file.txt")
print(f.read())
f.close()

# to not use this close statement we write like
with open("file.txt") as f:
    print(f.read())

# once we out of this with statement it will close automatally