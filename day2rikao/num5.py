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
    for i in klist:
        nlist.append(i.strip())
    mset=set()
    for k in nlist:
        mset.add(k)
    print(mset)

    mdict={}
    for j in mset:
        mcount=nlist.count(j)
        mdict[j]=mcount
    print(mdict)


