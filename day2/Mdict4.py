if __name__ == '__main__':
    mli=[1,2,3,1,2,1]
    md=dict()
    for i in mli:
        md.setdefault(i)
    print(md)

    for j in mli:
        md[j]=j
    print(md)

    for k in mli:
        mc=mli.count(k)
        md[k]=mc
    print(md)