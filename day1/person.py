
if __name__ == '__main__':
    i = 1 #当前行数
    ii = int(input("请输入:"))
    j = ii
    m = 0
    while i<=ii:
        while j>i:
            print(" ",end="")
            j -= 1
        print("*",end="")
        while m<2*i-3:
            print(" ",end="")
            m += 1
        if i!=1:
            print("*")
        else:
            print("")
        m = 0
        j = ii
        i += 1
    i = ii-1
    while i>=1:
        while j>i:
            print(" ",end="")
            j -= 1
        print("*",end="")
        while m<2*i-3:
            print(" ",end="")
            m += 1
        if i!=1:
            print("*")
        else:
            print("")
        m = 0
        j = ii
        i -= 1
