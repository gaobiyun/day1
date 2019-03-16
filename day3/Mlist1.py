if __name__ == '__main__':
    mli1=[]
    for i in range(1,11):
        mli1.append(i)
    print(mli1)
    
    mli=[i for i in range(1,11)]
    print("mli={mlikey}".format(mlikey=mli))


    mlis1=[]
    for i in range(1,11):
        mlis1.append(i*i)
    print(mlis1)

    mlis=[i*i for i in range(1,11)]
    print("mlis={mliskey}".format(mliskey=mlis))



    mlist1=[]
    for i in range(1,11):
        if i%2==0:
            mlist1.append(i)
    print(mlist1)

    mlist=[i for i in range(1,11) if i % 2==0]
    print("mlist={mlistkey}".format(mlistkey=mlist))