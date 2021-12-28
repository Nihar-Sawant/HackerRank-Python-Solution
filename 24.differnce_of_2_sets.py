# Enter your code here. Read input from STDIN. Print output to STDOUT
ip1=int(input())
a1=[int(i) for i in input().split()]
ip2=int(input())
a2=[int(i) for i in input().split()]
s1=set(a1)
s2=set(a2)
p=s1.difference(s2)
q=s2.difference(s1)
r=p.union(q)
res=list(r)
res.sort()
for i in res:
    print(i)
