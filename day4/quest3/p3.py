def user():
    em=input("请输入正确的邮箱地址:")
    if len(em)>=6 and "@" in em and "." in em:
        print("输入正确")
    else:
        print("姓名长度不能少于6位，邮件中包含@")
# if __name__ == '__main__':
#     user()