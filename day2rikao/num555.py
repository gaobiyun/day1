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
    #去除空格后的lkist放入pli
    pli=[i.strip() for i in klist]
    #放入集合
    mset=set(pli)
    md=dict()
    for j in mset:
        md.setdefault(j)
    print(md)