with open('input.txt', 'r', encoding='utf-8') as f:
    a9=0
    a10=0
    a11=0
    for line in f:
        s=line.split()
        if int(s[2])==9 & int(s[3])>a9:
            a9=int(s[3])
        elif int(s[2]) == 11:
            if int(s[3])>a11:
                a11 = int(s[3])
        elif int(s[2]) == 10 & int(s[3]) > a10:
            a10 = int(s[3])
    print(a9, a10, a11)