if __name__ == '__main__':
    str="good"
    #6为宽度 =为补齐
    s=str.ljust(6,"=")
    print(s)
    s1 = str.rjust(6, "=")
    print(s1)
    s2 = str.ljust(6)
    print(s2)
    s3 = str.rjust(8)
    print(s3)