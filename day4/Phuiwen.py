def huiWen():
    #从键盘输入一行字符串，判断是否是回文数（20分）
#（什么是回文数？例如，若n=1234321，
# 则称n为回文数；若n=1234，则n不是回文数）
    d=input("请输入数字判断是否为回文数")
    if d.__len__()%2==1:
        d1=d[::-1]
        if d==d1:
            print("{0}是回文数".format(d))
        else:
            print("不是回文数")
    else:
        print("回文数必须是奇数位")
if __name__ == '__main__':
    huiWen()