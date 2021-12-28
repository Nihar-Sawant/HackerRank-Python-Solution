def average(array):
    # your code goes here
    s=set(array)
    res=0
    for i in s:
        res+=i
    return res/len(s)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)