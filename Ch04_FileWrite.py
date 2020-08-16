lines = ["This is line 1", "This is line 2", "This is line 3"]

with open("test.txt", "w") as file:
    for line in lines:
        file.write(f"{line}\n")

with open("test.txt", "r") as fileRead:
    content = fileRead.read()
    print(content, end="")
    print("---")
    fileRead.seek(0)
    lines = fileRead.readlines()
    print(lines)
    print("---")
    for line in lines:
        print(line, end="")
    print("---")
    fileRead.seek(0)
    for line in fileRead:
        print(line, end="")
    print("-4-")
    fileRead.seek(0)
    print(fileRead.read())
