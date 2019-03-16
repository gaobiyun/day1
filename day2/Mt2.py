if __name__ == '__main__':
    str="11112222333355641234"
    mlist=list(str)
    print(mlist)
    nset=set(str)
    print(nset)
    for i in str:
        nset.add(i)
    print(nset)
    mset=list(nset)
    print(type(mset))

