with open("text.txt", "r") as f:
    size = 10
    fContents = f.read(size)

    # printing with multiple gaps
    while len(fContents) > 0:
        print(fContents, end="*")
        fContents = f.read(size)

    # tell gives the current position
    # seeks changes the position to a desired value

# File write
with open("test2.txt", "w") as file:
    file.write("This is a write test. Ore Shala")
    file.seek(0)
    file.write("Testis")
