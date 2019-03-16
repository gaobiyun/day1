if __name__ == '__main__':
    mset = {1, 2, 3, 3, 4,0}
    nset = {6, 5, 9, 3, 8}

    #并集  合并去重复的元素
    g=mset|nset
    print(g)

    # 交集  取共同元素
    f = mset & nset
    print(f)

    #差运算  留下减去共同元素的nset里的元素
    d = nset - mset
    print(d)

    d1 = nset ^ mset
    print(d1)