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
    for i in klist:
        nlist.append(i.strip())

    print(nlist)

    mset=set()
    for j in nlist:
        mset.add(j)
    print(mset)

    md=dict()
    for k in nlist:
        mc=nlist.count(k)
        md[k]=mc
    print(md)
