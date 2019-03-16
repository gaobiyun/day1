if __name__ == '__main__':
    # 字符串
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    nlist=[]
    for j in klist:
        nlist.append(j.strip())
    #放入集合
    print(nlist)
    mset=set(nlist)
    print(mset)
    #进行遍历
    for i in mset:
        #统计词频
        mcount = nlist.count(i)
        if mcount>=2:
            print("{0}出现次数{1}".format(i,mcount))