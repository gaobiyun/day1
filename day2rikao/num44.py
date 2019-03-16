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
    nli=[i.strip() for i in klist]
    mset=set(nli)
    md=dict()
    for j in mset:
        mcount = nli.count(j)
        md[j]=mcount
       # md.setdefault(j,mcount)
    print(md)