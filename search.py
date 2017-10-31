#tim kiem nhi phan

a = [1,2,3,4,5,6,7,8,9,10]


def binary_search(x, a, first, last):
    while(first <= last):
        mid = (first + last)//2
        if(x == a[mid]):
            return mid
        elif(x < a[mid]):
            return binary_search(x, a, first, mid-1)
        else:
            return binary_search(x, a, mid+1, last)
    
    return -1

def tim_kiem_thong_thuong(x, a):
    count = 0
    for i in range(len(a)):
        if(x == a[i]):
            return i
    return -1


print(binary_search(8, a, 0, len(a)))
