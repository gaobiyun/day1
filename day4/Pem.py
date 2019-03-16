def Email():
    put=input("请输入邮箱：")
    if int(put.find("@"))>0:
        if put[0:7].__len__()>=6:
            if put.endswith(".com") or put.endswith(".cn"):
                print("邮箱正确")
            else:
                print("请以“com” 或“cn”为后缀")
        else:
            print("请输入6位或以上的邮箱名字")
    else:
        print("您输入的邮箱缺少“@”符号")
if __name__ == '__main__':
    Email()