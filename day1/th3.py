if __name__ == '__main__':
    uname="gby"
    upassword=12
    usex="man"
    #纯输出 默认每个字符间为一个空格
    print(uname,upassword,usex)
    #加入间隔符
    print(uname,upassword,usex,sep="=")
    #去掉间隔
    print(uname,upassword,usex,sep="")
    #下一行不换行
    print(uname,upassword,usex,end=" ")
    print(uname,upassword,usex,sep="")