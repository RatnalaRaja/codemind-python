a = int(input())

x = list(map(int,input().split()))
sum_ = 0
for i in x:
    sum_+=i
print(int(sum_/a) in x)