if __name__ == '__main__':
    #创建文件
    f=open(r"F:\us.txt","w")
    mli=str([i for i in range(1,50)])
    print(f.writable())
    f.write("hukskldj ksd jfkjs f")
    f.writelines("555555555555")
    f.writelines(mli)


    f.close()


