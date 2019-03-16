import random
def elist():
    mlist = [random.randint(1, 31) for i in range(0, 10)]
    nlist=[random.randint(1, 31) for i in range(0, 15)]
    mset=set(mlist)
    nset=set(nlist)
    #print(mlist)
    #print(nlist)
    gs=mset^nset
    print(gs)
# if __name__ == '__main__':
#     elist()



