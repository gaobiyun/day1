if __name__ == '__main__':
    str="good good study"
    #d出现几次
    s=str.count("d")
    print(s)
    #从4开始寻找d出现的次数
    ss=str.count("d",4)
    print(ss)
    #从4到9 d出现的次数
    sss=str.count("d",4,9)
    print(sss)