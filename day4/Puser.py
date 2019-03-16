#注意一个用户信息，包含EMAIL号，判断信息是否合法，
# 如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）（30分）
def Email():
    put=input("请输入邮箱：")
    if (put.find("@"))>0:
        if (put.find("."))>0:
            if put[0:7].__len__() >= 6:
                print("您输入的邮箱合法")
            else:
                print("姓名长度必须为6位或以上")
        else:
            print("邮箱格式中缺少 “.” 符号")
    else:
        print("邮箱格式中缺少 “@” 符号")
if __name__ == '__main__':
    Email()