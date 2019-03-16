if __name__ == '__main__':
    mli=[1,2,3]
    md=dict()
    for i in mli:
        md.setdefault(i)
    print(md)