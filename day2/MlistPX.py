import random
if __name__ == '__main__':
    mlist = [3,5,2,6,1,8,0]
    #随机打乱  必须导包
    random.shuffle(mlist)
    print(mlist)
    #升序排序 永久性排序 后面调用此排序后的列表
    mlist.sort()
    print(mlist)
    #降序
    mlist.sort(reverse=True)
    print(mlist)
    #临时排序 后面调用列表还是初始列表
    sorted(mlist,reverse=True)
    print(mlist)
    #永久性的反转
    mlist.reverse()
    print(mlist)