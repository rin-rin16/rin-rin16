d={i: chr(i) for i in range(ord('a'), ord('z')+1)}
print(d)
d.update({i: chr(i) for i in range(ord('A'), ord('Z')+1, 1)})
print(d)