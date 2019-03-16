if __name__ == '__main__':
    str="123456421215115"
    mset=set()
    for i in str:
        mset.add(i)
    print(mset)
    print(mset.__len__())
    print(str.__len__())
    if mset.__len__()<str.__len__():
        print("该字符串重复")
    else:
        print("该字符串不重复")
