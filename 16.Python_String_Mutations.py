def mutate_string(string, position, character):
    res=[]
    string2=""
    for i in string:
        res.append(i)
    res.insert(position,character)
    res.pop(position+1)
    for i in res:
        string2+=i    
    return string2

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)