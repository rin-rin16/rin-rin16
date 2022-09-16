with open('input.txt', 'r', encoding='utf-8') as f:
    a = list(map(lambda x: x.rstrip().split(), f.readlines()))
    a.sort(key = lambda x: x[0])
    print(a)