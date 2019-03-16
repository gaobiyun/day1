import  random
if __name__ == '__main__':
    shu=input("输入整数")
    shu=int(shu)
    print(type(shu))
    v=random.randint(1,10)
    print(v)
    print(type(v))
    if(shu>v):
        print(shu,">",v)
    elif(shu==v):
        print(shu,"=",v)
    elif(shu<v):
        print(shu,"<",v)