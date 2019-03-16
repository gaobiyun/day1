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

    if mset.__len__()<klist.__len__():
        print("重复")
    else:
        print("没有重复")