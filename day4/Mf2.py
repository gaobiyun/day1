if __name__ == '__main__':
    f = open(r"F:\us.txt", "r+")
    print(f.readable())
    print(f.read())

    f.close()