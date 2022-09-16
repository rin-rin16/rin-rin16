s=list(input().split())
a=set(s[0])
for i in range(1, len(s)):
    a &= set(s[i])
print(a)