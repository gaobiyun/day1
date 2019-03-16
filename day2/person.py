if __name__ == '__main__':
    s="ssdjfhgsdfhjkjsdfaweryyuui"
    d=set()
    for i in s:
        d.add(i)
    for i in d:
        num=s.count(i)
        if num>=2:
            print("重复的是{0},重复的次数为：{1}".format(i,num))