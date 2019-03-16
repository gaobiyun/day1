if __name__ == '__main__':
    #两种方式创建列表
    mlist=list()
    mlist1 = []
    print(type(mlist))
    print(type(mlist1))
    #末尾追加数据
    mlist.append("贾梦瑶")
    print(mlist)
    #指定位置加入数据 即索引 下标
    mlist.insert(0,"小傻蛋")
    print(mlist)
    #添加元素
    mlist.insert(1, "小傻蛋")
    print(mlist)
    #删除元素
    mlist.pop()
    print(mlist)
    #根据索引删除元素
    del mlist[2]
    print(mlist)
    #移除该数据  如果该元素不存在 则报错
    mlist.remove("小傻蛋")
    print(mlist)
    #清空列表内容 留下对象
    mlist.clear()
    print(mlist)