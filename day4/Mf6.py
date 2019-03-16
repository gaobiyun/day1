if __name__ == '__main__':
    with open(r"F:\u1.txt","w+") as f:
        mk=str([i for i in range(1,20)])
        f.writelines(mk)
        ml=f.readline()
        print(mk)
        print(ml)