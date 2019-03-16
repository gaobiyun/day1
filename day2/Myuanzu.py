if __name__ == '__main__':
    mtuple=(1,2,3,4,5)
    #如果只有一个元素，必须加逗号
    ktuple=(10,)
    #遍历
    for i in mtuple:
        print(i,end="")

    #切片
    ntuple=mtuple[2:1:-1]
    print(ntuple)

    #id值
    print(id(mtuple))
    print(id(ntuple))
    print(id(ktuple))