d={i: chr(i) for i in range(ord('a'), ord('z')+1)}
d.update({i: chr(i) for i in range(ord('A'), ord('Z')+1, 1)})
dict={d[i]: i for i in range(97, 123)}
print(dict)