import itertools as it
with open("output.txt", "w") as t:
    with open("input.txt", "r") as f:
        a = list(map(lambda x: x.rstrip().split(), f.readlines()))
    b=list(it.zip_longest(*a, fillvalue=0))
    for column in range(len(b)):
        k=[]
        for g in range(len(b[column])):
            k.append(int(b[column][g]))
        t.write(str(sum(k))+' ')