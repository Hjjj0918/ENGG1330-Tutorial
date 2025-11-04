def binStr(n:int, prev:list):
    if len(prev) == n:
        print(prev)    

    else:
        binStr(n, prev + [0])
        binStr(n, prev + [1])


def main():
    n = int(input())
    binStr(n, [])

main()