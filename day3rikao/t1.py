if __name__ == '__main__':
    a=(input("输入第一个人生日:"))
    print(a)
    b = (input("输入第二个人生日:"))
    print(b)
    c=int(a[0:4])
    print(c)
    d=int(b[0:4])
    print(type(d))
    if c-d>0:
        print("c年龄大")
    elif c-d<0:
        print("d年龄大")
    elif c==d:
        print("同岁")