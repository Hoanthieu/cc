#bai toan day con chung dai nhat


'''
Phan tich 1 ty
 thuat toan truc tiep la duyet tat ca cac day con co the co cua A, so khop voi B
 nen do phuc tap len den n*2^m

 Giai thuatj tien bo hon:
 goi c[i][j] la do dai day con chung dai nhat cua 2 day (x1, x2, .., xi) va
   (y1, y2,..., yj)
   Khi do, co (m+1, n+1) bai toan con
   Bai toan lon nhat la tim c(m, n)

   khoi tao
   c[0][j] = 0 voi moi j
   c[i][0] = 0 voi moi i

   Duyet tung phan tu cua 2 mang x va y
   Neu xi = yj thi c[i][j] = 1 + c[i-1][j-1]
   Neu xi != yj thif c[i][j] = max{c[i-1][j], c[i][j-1]}

'''

#Implement

X = ['a', 'b', 'c', 'b']
Y = ['b', 'd', 'c', 'a', 'b']
m = len(X)
n = len(Y)


c = []
for i in range(m+1):
    hang = []
    for j in range(n+1):
        hang.append(0)
    c.append(hang)

for i in range(m):
    for j in range(n):
        if (X[i] == Y[j]):
            c[i+1][j+1] = c[i][j] + 1
        else:
            c[i+1][j+1] = max(c[i][j+1], c[i+1][j])

print(c[m][n])
for i in range(m+1):
    print(c[i])
        
       
