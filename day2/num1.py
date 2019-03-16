if __name__ == '__main__':
    num=range(1,10)
    nam=str(num)

    for i in num:
        for j in num:
            if i*j>10:
                nam.rjust(i,"*",j,"=",i*j,end=" ")
            if i==j:
                print()
                break


