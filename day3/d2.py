def numberArray():#随机输入数字进行规则排列
    en = int(input("请输入要排列到的位置，从0开始:"))
    for i in range(0,en+1) :
        print(str(i).rjust(4," "),end=" ")
        if i % 10 == 9:
            print()
if __name__ == '__main__':
    numberArray()