while True:
    try:
        amount = float(input("Change owed: "))
    except:
        continue
    else:
        if amount > 0:
            break

amount = amount * 100
change = 0

while True:
    if amount >= 25:
        amount = amount - 25
        change += 1
    elif amount >= 10:
        amount = amount - 10
        change += 1
    elif amount >= 5:
        amount = amount - 5
        change += 1
    elif amount >= 1:
        amount = amount - 1
        change += 1
    else:
        break

print(change)
