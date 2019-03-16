def fun1():
    pass
    print("这是函数1")


def fun2():
    print("这是函数2")


def fun3():
    print("这是函数3")


def fun4():
    print("这是函数4")


if __name__ == '__main__':
    mdict1 = {  # 提示功能字典1
        1: "[1]输入用户姓名及性别，然后给出下列的提示",
        2: "[2]随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
        3: "[3]注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）",
        4: "[4]从键盘输入一行字符串，判断是否是回文数"
    }
    mdict2 = {  # 储存函数字典2
        1: fun1,
        2: fun2,
        3: fun3,
        4: fun4
    }

    for i in mdict1.values():  # 输出字典1提示内容
        print(i)

    msel = int(input("请选择功能"))

    for k in mdict1.keys():
        if msel == k:
            print("你选择的是:{mdict1key}".format(mdict1key=k))
            mdict2[k]()  # 加()实现反向索引