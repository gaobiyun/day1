if __name__ == '__main__':
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
    for k in klist:
        nlist.append(k.strip())
    print(nlist)

    mset=set()
    for i in nlist:
        mset.add(i)

    print(mset)

    md=dict()
    for j in mset:
        mc=nlist.count(j)
        md[j]=mc
    print(md)