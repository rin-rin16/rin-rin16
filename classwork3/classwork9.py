a=input()
l=[]
for char in a:
    l += char
l1=[]
for i in range(len(l)):
    if l[i] == ' ' or l[i].isdigit():
        continue
    else:
        l1.append(l[i])
dic={}
for i in l1:
    if i in dic:
        dic[i] += 1/len(l)
    else:
        dic[i] = 1/len(l)
print(dic.items())