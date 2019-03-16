if __name__ == '__main__':
    str="ahsbsjbskjbasj"
    mset=set(str)
    print(mset)
    mset = set()
    for j in str:
        mset.add(j)
    for i in mset:
        mcount=str.count(i)
        if mcount>=2:
            print("重复的为{0}，重复次数为:{1}".format(i,mcount))