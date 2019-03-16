if __name__ == '__main__':
    str = "good good study"
    #用gud替换good
    s = str.replace("good","gud")
    print(s)
    # 用gud替换good  最多一次
    ss=str.replace("good","gd",1)
    print(ss)