m = [[1, 2, 3], [4, 5, 6]]
r = []
for i in range(len(m[0])):
    f = []
    for j in range(len(m)):
        f.append(m[j][i])
    r.append(f)
print(r)
 