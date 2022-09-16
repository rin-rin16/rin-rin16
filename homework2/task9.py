with open('input.txt', 'r', encoding='utf-8') as f:
    a9=a10=a11=c9=c10=c11=0
    for line in f:
        s=line.split()
        if int(s[2]) == 9:
            a9 += int(s[3])
            c9 += 1
        elif int(s[2]) == 11:
                a11 += int(s[3])
                c11 += 1
        elif int(s[2]) == 10:
            a10 += int(s[3])
            c10 += 1
    print(a9/c9, a10/c10, a11/c11)