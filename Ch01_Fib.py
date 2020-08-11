def main():
    n = int(input("n: "))
    for x in range(1, n+1):
        print(fibFind(x))
    print(fibList(1))
    print(fibList(2))
    print(fibList(n))


def fibFind(n):
    fibX, fibNext = 1, 1
    if n <= 2:
        return 1

    i = 3
    while i <= n:
        i += 1
        fibX, fibNext = fibNext, fibX + fibNext
    return fibNext


def fibList(n):
    fibLs = [1, 1]
    fibX, fibNext = 1, 1
    if n == 1:
        return [1]
    elif n == 2:
        return fibLs
    i = 3
    while i <= n:
        i += 1
        fibX, fibNext = fibNext, fibX + fibNext
        fibLs.append(fibNext)
    return fibLs


if __name__ == "__main__":
    main()
