a,b=map(int,input().split())
n=set(list(map(int,input().split())))
m=set(list(map(int,input().split())))
s=n.intersection(m)
print(len(s))