if __name__ == '__main__':
    arr=[1,2,3]
    for i in arr:
        print(i, end=" ")  #123
        for j in arr:
            print(i,end=" ")    #111  222 333
            print("==========")
            print(j,end=" ")    #123 123 123
