if __name__ == '__main__':
    mli=[1,2,3]
    nli=["A","B","C"]
    kli=[]
    for i in mli:
        for j in nli:
            kli.append(str(i)+j)
    print(kli)



    klist=[ str(i) + j for i in mli for j in nli]
    print(klist)


    dlist=[str(i)+j
           for i in mli \
            if i%2!=0 \
           for j in nli]
    print(dlist)