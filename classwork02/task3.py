from collections import *
with open("output.txt", "w") as t:
    with open("input.txt", "r") as f:
        a = list(map(lambda x: x.rstrip().split(), f.readlines()))
        s=[]
        for i in range(len(a)):
            s.extend(a[i])
        p=Counter(s)
        sus=list(p.most_common(7))
        gus=[sus[i][0] for i in range(0, len(sus), 1)]
        for i in range(len(gus)):
            print(gus[i], end=' ')