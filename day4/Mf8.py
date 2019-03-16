if __name__ == '__main__':
    with open(r"F:\u2.txt","r+") as f:
        k=str([j for j in range(20,60,3)])
        #f.writelines(k)

        fe=list(f)
        print(fe)
        c=f.read()
        print(c)
