if __name__ == '__main__':
    mlist = {1, 2, 3, 5, 4, 9, 0, 7}
    #增加元素
    mlist.add(20)
    print(mlist)
    #修改集合
    mlist.update({90,50,40})
    print(mlist)
    #复制
    nlist=mlist.copy()
    print(nlist)

    nlist.remove(3)
    print(nlist)