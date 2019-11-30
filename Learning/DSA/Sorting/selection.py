def selection(a):
    for i in range(len(a)):
        small = i
        for j in range(i+1, len(a)):
            if a[small]>a[j]:
                small = j
        a[small], a[i] = a[i], a[small]
    return a

arr = [5,3,7,2,1]
print(selection(arr))