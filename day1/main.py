if __name__ == '__main__':
    str=9
    if str==9:
        print(1)
    elif str==8:
        print(2)
    else:
        print(3)
    score=0;
    mscore=input("输入成绩:")
    mscore=int(mscore)
    if mscore<=100 and mscore>0:
        if mscore>=90:
            print("优秀")
        if mscore>=60 and mscore<90:
            print("还行")
        if mscore<60:
            print("重修")
