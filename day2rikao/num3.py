if __name__ == '__main__':
    #字符串
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
    #将klist放入集合 排重
    kset =set(klist)
    #判断 如果集合长度小于klist长度 有重复元素 否则不重复
    if kset.__len__()<klist.__len__():
        print("有重复元素")
    else:
        print("不重复")

