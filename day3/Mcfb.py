def fu(i,j):
    return i*j

if __name__ == '__main__':
    for i in range(1,10):
        for j in range(1,10):
            if j<=i:
                s = str(i * j)
                s=s.rjust(2, " ")
                print(j, "*", i, "=", s, end="  ")
            else:
                print()
                break

