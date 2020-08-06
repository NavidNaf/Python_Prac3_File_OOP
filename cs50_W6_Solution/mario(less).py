while True:
    try:
        height = int(input("Height:"))
    except:
        continue
    else:
        if height > 0 and height < 9:
            break

for i in range(height):
    print(" " * (height - i - 1), end="")
    print("#" * (i + 1))
