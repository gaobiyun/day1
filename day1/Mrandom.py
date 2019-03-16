import  random
if __name__ == '__main__':
    #随机一个整型值
    n=random.randint(4,9)
    print(n)
    #随机出现的一个数值
    v=random.choice(range(10))
    print(v)
    #
    s=random.randrange(1,10)
    print(s)
    #随机出现的浮点数 实数
    h=random.uniform(1,2)
    print(h)