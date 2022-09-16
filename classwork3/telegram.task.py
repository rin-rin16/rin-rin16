N = float(input())
a = input()
l=list(a.split(' '))
l1 = [float(l[i]) for i in range(len(l))]
s = {l1[i] for i in range(len(l1))}
lfin = [i for i in s]
for i in range(0, len(lfin)-1, 1):
    for j in range(i+1, len(lfin), 1):
        if lfin[i] + lfin[j] == N:
            print(lfin[i], lfin[j])
half = 0
if N != 0:
    for i in range(0, len(l1)-1, 1):
        for j in range(i+1, len(l1), 1):
            if l1[i] == l1[j] and l1[i] + l1[j] == N:
                half=l1[i]
    if half != 0:
        print(half, half)
k = 0
if N == 0:
    for i in l1:
        if i == 0:
            k +=1
    if k>=2:
        print(0, 0)