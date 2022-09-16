a=input()
s=set()
for char in a:
    s |= {char}
k=0
for i in s:
    k += ord(i)
print(k)