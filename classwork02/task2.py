import itertools as it
with open("output.txt", "w") as t:
    with open("input.txt", "r") as f:
        a = list(map(lambda x: x.rstrip().split(), f.readlines()))
    k=int(a[0][0])
    for i in it.count(1, 1):
        if i==len(a):
            break
        else:
            t.write(str((i-1)%k))
            t.write(' ')
            t.write(str(' '.join(a[i])))
            t.write('\n')