if __name__ == '__main__':
    mlist = [1, 2, 3, 5, 4, 9, 0, 7]
    print(id(mlist))

    nlist=mlist
    print(id(nlist))

    #切片 全切
    hlist=mlist[:]
    print(id(hlist))
