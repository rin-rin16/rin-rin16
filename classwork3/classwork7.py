n = int(input())
d = dict()
for i in range(n):
    s = input()
    p=list(s.split())
    d.update({p[0]: p[1]})
s = input()
print(d[s])