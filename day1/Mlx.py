if __name__ == '__main__':

    m9=[1, 2, 3, 4, 5, 6, 7, 8]
    for i in m9:
        for j in m9:
            if i<j:
                print(" ",end=" ")
        for h in m9[0:i-1]:
            print("*",end=" ")

        for k in m9:
            print("*", end=" ")
            if k==i:
                print()
                break

    for u in m9:
        for l in m9:
            print(" ",end=" ")
            if u==l:
                break
        for r in m9:
            if u<r:
                print("*",end=" ")
                if u<r-1:
                    print("*", end=" ")
        print()


