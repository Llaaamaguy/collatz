import math

solved = {}

def collatzAlgorithm(n):
    if n % 2 == 1:
        return 3 * n + 1
    else:
        return n // 2

def append_value(dict_obj, key, value):
    if key in dict_obj:
        dict_obj[key].append(value)
    else:
        dict_obj[key] = [value]

def collatz(n):
    chain = n
    nextValue = n
    while nextValue != 1:
        nextValue = collatzAlgorithm(nextValue)
        if nextValue not in solved:
            append_value(solved, chain, nextValue)
        else:
            append_value(solved, chain, nextValue)
            solved[chain].extend(solved[nextValue])
            break


def Log2(x):
    if x == 0:
        return False

    return (math.log10(x) /
            math.log10(2))

def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) ==
            math.floor(Log2(n)))


def main():
    for i in range(1,10001):
        collatz(i)
    print("Longest collatz chain between 2 and 10,000:")
    length = 0
    for key, i in solved.items():
        if len(i) > length:
            lchain = i
            lkey = key
            length = len(i)
    print(lkey, lchain)
    length = 300

    print("\n Shortest collatz chain that is not a power of 2")
    for key, i in solved.items():
        if isPowerOfTwo(key) == False:
            if len(i) < length:
                schain = i
                skey = key
                length = len(i)
    print(skey, schain)
    length = 0

    print("\n Average length of chains from 2 to 10,000")
    lenlist = []
    for key, i in solved.items():
        lenlist.append(len(i) + 1)
    average = sum(lenlist) / len(lenlist)
    print(average)


if __name__ == "__main__":
    main()