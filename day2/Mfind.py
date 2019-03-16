if __name__ == '__main__':
    #索引从0开始 空格算一个索引
    str="good good study"
    #寻找study字符串位置 返回出现字符串位置的下标
    st=str.find("study")
    print(st)
    #根据下标为4开始寻找 oo出现的索引
    stt=str.find("oo",4)
    print(stt)
    #留头不留尾  从1到3范围寻找d出现的索引
    sttt=str.find("d",1,3)
    print(sttt)