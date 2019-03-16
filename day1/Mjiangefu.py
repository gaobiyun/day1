if __name__ == '__main__':
    uname="hehe"
    upassword="hehe"
    usex="man"
    #正常输出   自动换行  默认一个空格为间隔符
    print(uname,upassword,usex)
    #输出下一行不换行 end=""
    print(uname,upassword,usex,end="")
    print("==============")
    #没有空格间隔符 sep=""
    print(uname,upassword,usex,sep="")