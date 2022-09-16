import collections as coll
with open('input.txt', 'r', encoding='utf-8') as f:
    k=0
    for line in f:
        s = line.split()
        if int(s[3])>k:
            k=int(s[3])
    l=[]
    f.seek(0)
    for line in f:
        s = line.split()
        if int(s[3])==k:
            l.append(s[2])
    lis=list(coll.Counter(l))
    for i in range(len(lis)):
        print(lis[i], end=' ')