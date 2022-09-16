with open('input.txt', mode='r') as f:
    a=list(map(lambda x: x.rstrip().split(), f.readlines()))
    for i in range(len(a)):
        print(' '.join(a[len(a)-i-1]))