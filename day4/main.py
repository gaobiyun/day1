import day4.quest1.p1 as pone
import day4.quest2.p2 as ptwo
import day4.quest3.p3 as pthr
import day4.quest4.p4 as pfour
if __name__ == '__main__':
    md={1:"输入用户姓名及性别，然后给出下列的提示"  ,
        2:"随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集" ,
        3:"注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）",
        4:"从键盘输入一行字符串，判断是否是回文数"
        }

    while True:
        s = int(input("输入序号"))
        if s==1:
            pone.checkSex()
        elif s==2:
            ptwo.elist()
        elif s==3:
            pthr.user()
        elif s==4:
            pfour.num()
        else:
            print("没有该项选择")




