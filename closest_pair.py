#chia de tri tim cap diem gan nhat

import math
import random
import time

mang = []
for i in range(5000):
    mang.append([1000*random.random(), 1000*random.random()])

def dist(a, b):
    return math.sqrt((a[0] - b[0])*(a[0] - b[0]) +
                     (a[1] - b[1])*(a[1] - b[1]))

def vetcan(mang):
    n = len(mang)
    maxDist = 10000000
    for i in range(n-1):
        for j in range(i+1, n):
            if maxDist > dist(mang[i], mang[j]):
                maxDist = dist(mang[i], mang[j])
    return maxDist
current = time.time()
m = vetcan(mang)
cr = time.time()
print('vetccan ', m, ' with ', cr - current)


#chia de tri lieu co tot hon
mang.sort(key = lambda x:x[0])
n = len(mang)

#thuat toan chinh la chia thanh 2 mang con, tim khoang cach nho nhat cua 2 cai do
#luu vao 1 cai strip, roi tim min trong cai strip do

def stripClosest(mang, d):
    n = len(mang)
    mini = d
    for i in range(n):
        for j in range(i+1, n):
            if(mang[j][1] - mang[i][1] < mini):
                if(dist(mang[i], mang[j]) < mini):
                    mini = dist(mang[i], mang[j])

    return mini



def chiadetri(mang):
    n = len(mang)
    if n <= 3:
        return vetcan(mang)
    else:
        m = n//2
        midPoint = mang[m]
        mang1 = mang[:m]
        mang2 = mang[m:]
        dl = chiadetri(mang1)
        dr = chiadetri(mang2)
        min_local = min(dl, dr)
        cc = []
        #tim cac diem co kha nang co kc tung doi < min_local o ca 2 phia cua mang
        for i in range(n):
            if(mang[i][0] - midPoint[0] < min_local):
                cc.append(mang[i])
        return min(min_local, stripClosest(cc, min_local))
                

current2 = time.time()
m = chiadetri(mang)
cr2 = time.time()
print('chia de tri: ',chiadetri(mang),' with ', cr2 - current2)
        

    
