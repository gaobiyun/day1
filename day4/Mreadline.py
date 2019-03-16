if __name__ == '__main__':
    f=open(r"F:\u.txt","r+")
    mli = f.readline()
    print(mli)
    #已经读完 所以为空
    nli = f.readlines()
    print(nli)
    f.close()