def checkSex():
    uname=input("请输入姓名:")
    usex=input("请输入性别")
    nlist=["Mr","Boy","Man","男"]
    mlist=str(["Miss","Girl","Women","女"])
    md=dict()
    if usex in nlist:
        print("{unamekey}先生你好".format(unamekey=uname))
    elif usex in mlist:
        print("{unamekey}女士你好".format(unamekey=uname))
    else:
        print("输入性别有误")

# if __name__ == '__main__':
#     checkSex()