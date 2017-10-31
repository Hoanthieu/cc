#mang con lon nhat

def maxLeft(a, first, last):
    maxSum = -101010101
    tong = 0
    for i in range(last-1, first-1, -1):
        tong += a[i]
        if maxSum < tong:
            maxSum = tong
    return maxSum
        

def maxRight(a, first, last):
    maxSum = -101010101
    tong = 0
    for i in range(first, last):
        tong += a[i]
        if maxSum < tong:
            maxSum = tong
    return maxSum

def maxSubVector(a, first, last):
    print(first, last)
    if first == last:
        return a[first]
    m = (first + last)//2
    wL = maxSubVector(a, first, m)
    wR = maxSubVector(a, m+1, last)
    wM = maxLeft(a, first, m) + maxRight(a, m+1, last)
    return max(wL, wR, wM)


a = [1,3,-2, 4, 10, -15, 20]
print(maxSubVector(a, 0, len(a)-1))

def mangconMax(a, first, last):
    maxSum = -100000000
    for i in range(first, last):
        s = 0
        for j in range(i+1, last):
            s += a[j]
            if maxSum < s:
                maxSum = s

    return maxSum

print(mangconMax(a, 0, len(a)))
