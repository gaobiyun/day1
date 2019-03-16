if __name__ == '__main__':
    with open(r"F:\u.txt","r+") as f:
        k=f.seek(0,2)
        print(k)