with open('input.txt', mode='r') as f:
    a=f.read().rstrip()
    for i in range(len(a)):
        print(a[len(a)-1-i], end='')