def db():
    b = input("输入边")
    b = int(b)
    for i in range(1, b + 1):
        for j in range(1, b + 1):
            print("*", end="")
            if i == j:
                print()
                break
