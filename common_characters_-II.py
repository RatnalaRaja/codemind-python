s1=input().lower().replace(' ','')
s2=input().lower().replace(' ','')
c=0
temp =[]
for i in s1:
    if i in s2 and i not  in temp:
        temp.append(i)

for i in s2:
    if i  in s1 and i not  in temp:
        temp.append(i)
for i in sorted(temp):
    c+=1
print(c)