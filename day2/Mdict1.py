if __name__ == '__main__':
    mdict={"name":"m","password":"pwd"}
    #通过键获取值
    print(mdict["name"])
    print(mdict.keys())
    print(mdict.values())
    print(mdict.items())

    #修改  通过键修改值   键必须不可变
    mdict["name"]="sex"
    print(mdict)

    #删除键name
    del mdict["name"]
    print(mdict)

    #长度
    print(len(mdict))
    #转换字符串格式
    ndict=str(mdict)
    print(ndict)
    print(type(ndict))