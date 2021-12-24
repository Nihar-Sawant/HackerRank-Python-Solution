if __name__ == '__main__':
    s = input()
    alnum=False
    alpha=False
    digi=False
    low=False
    up=False
    for i in s:
        if(i.isalnum()):
            alnum=True
        if(i.isalpha()):
            alpha=True
        if(i.isdigit()):
            digi=True
        if(i.islower()):
            low=True
        if(i.isupper()):
            up=True
    print(alnum)
    print(alpha)
    print(digi)
    print(low)
    print(up)