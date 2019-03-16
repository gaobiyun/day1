def nineTable():#九九乘法表
    for x in range(1,10) :
        for y in range(1,10):
            if y <= x :
                z = str(x*y)
                z = z.rjust(2," ")
                print(x,"*",y,"=",z,end=" ")
            else:
                print()
                break
if __name__ == '__main__':
    nineTable()