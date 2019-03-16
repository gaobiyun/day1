if __name__ == '__main__':
    mset = {1, 2, 3,"good", 3,"luck", 4}
    for i in mset:
        print(i)

    nset={(1,2,3),(2,3,3),(6,9,3)}
    #n,q,r对应元祖元素的数量
    for n,q,r in nset:
        print(n,q,r)

    mset = {1, 2, 3, 3, 4}
    nns={i for i in mset}
    print(nns)

    mset = {1, 2, 3, 3, 4}
    s={i for i in mset if i%2==0}
    print(s)