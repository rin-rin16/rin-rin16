s=list(input().split())
a=set(s[0])
i=1
while i<len(s):
    a &= set(s[i])
    i += 1
print(a)