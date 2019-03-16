def num():
    s=input("输入数字:")
    if len(s) %2!=0:
        mli = [i for i in s]
        nli = mli[:]
        print(nli)
        mli.reverse()
        print(mli)
        if nli == mli:
            print("是回文数")
        else:
            print("不是回文数")
    else:
        print("输入不符合条件")

# if __name__ == '__main__':
#         num()