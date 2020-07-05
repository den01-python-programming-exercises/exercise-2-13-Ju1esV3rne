def main():
    pos = 0
    neg = 0
    point = 0
    while True:
        num = int(input())
        if num == 0:
            break
        elif num>0:
            pos = pos + num
            point += 1
        elif num<0:
            neg = neg + num
    if pos == 0:
        print("Cannot calculate the average")
    else:
        print(pos/point)


if __name__ == '__main__':
    main()
