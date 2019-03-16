import random
def s():
    nli=[j for j in range(1,20)]
    random.shuffle(nli)
    #print(nli)
    k=nli
if __name__ == '__main__':
    mlist = [i for i in range(1, 50)]
    random.shuffle(mlist)
    print(mlist)
    #创建文件
    f = open(r"F:\u.txt", "w+")
    f.writelines(str(mlist))
    f.close()