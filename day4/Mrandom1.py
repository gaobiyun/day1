import random
if __name__ == '__main__':
    nli = list()
    for j in range(1, 20):
        nli.append(j)
    random.shuffle(nli)
    print(nli)