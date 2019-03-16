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
    #复制
    vlist=klist[:]
    #定义空的列表
    nli=[]

    for i in klist:
        #去除空格后 放入nli
        nli.append(i.strip())
    #放进集合 去重
    mset=set(nli)


    # pli = []
    # for k in vlist:
    #     pli.append(k.strip())
    # nset=set(pli)

    # 空字典
    md = dict()
    for j  in mset:
        md[j] = j
    print(md)