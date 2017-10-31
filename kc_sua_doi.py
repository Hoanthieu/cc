a = 'exponential'
b = 'polynomial'
m = len(a)
n = len(b)
d = []
for i in range(m+1):
    vect = []
    for j in range(n+1):
        vect.append(0)
    d.append(vect)

for i in range(m+1):
    d[i][0] = i

for i in range(n+1):
    d[0][i] = i
for i in range(1, m+1):
    for j in range(1, n+1):
        if(a[i-1] != b[j-1]):
            d[i][j] = min(d[i-1][j-1] + 1, d[i-1][j] + 1, d[i][j-1] + 1)
        else:
            d[i][j] = min(d[i-1][j-1], d[i-1][j]+1, d[i][j-1] + 1)

print('    ', b.split())
print('  ',d[0])
for i in range(1, m+1):
    print(a[i-1], d[i])
