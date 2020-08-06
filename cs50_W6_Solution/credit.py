while True:
    try:
        numb = int(input("Number: "))
    except:
        continue
    else:
        if numb > 0:
            break


def checksum(number):
    numbtoStr = str(number)
    lsNumb = []
    newNumb = []
    lsothNumb = []
    addition = 0
    addition1 = 0
    numbtoStr = numbtoStr[::-1]
    length = len(numbtoStr)
    # print(numbtoStr)
    for i in numbtoStr[1:length:2]:
        lsNumb.append(int(i) * 2)
    # print(lsNumb)
    newlen = len(lsNumb)
    for i in range(newlen):
        if lsNumb[i] > 9:
            newi = lsNumb[i] // 10
            newir = lsNumb[i] % 10
            lsNumb.append(newi)
            lsNumb.append(newir)
    for i in lsNumb:
        if i < 9:
            newNumb.append(i)
    # print(newNumb)
    for i in numbtoStr[0:length:2]:
        lsothNumb.append(int(i))
    # print(lsothNumb)
    for i in newNumb:
        addition += i
    for i in lsothNumb:
        addition1 += i
    total = addition + addition1
    modulo = total % 10

    if modulo == 0:
        return True
    else:
        return False


# checksum(numb)
# print(checksum(numb))
numbtoStr = str(numb)
length = len(numbtoStr)

if checksum(numb) == True:
    if (length == 13 or length == 16) and numbtoStr[0] == "4":
        print("VISA")
    elif length == 15 and numbtoStr[0] == "3" and (numbtoStr[1] == "4" or numbtoStr[1] == "7"):
        print("AMEX")
    elif length == 16 and numbtoStr[0] == "5" and (numbtoStr[1] == "1" or numbtoStr[1] == "2" or numbtoStr[1] == "3" or numbtoStr[1] == "4" or numbtoStr[1] == "5"):
        print("MASTERCARD")
else:
    print("INVALID")
