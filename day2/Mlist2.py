if __name__ == '__main__':
    mlist=[1,2,3,5,4,9,0,7]
    for i in mlist:
        print(i,end="")

#     #改变列表索引为2的值为9
    mlist[2]=9


    for j in mlist:
        print(j,end="")

if __name__ == '__main__':
    mlist=[1,2,3,5,4,9,0,7]

    print(mlist[2].__index__())
    print(("mlist[{0}]={1}").format(mlist[3].__index__(),mlist[3]))