def insertion(a):
    for i in range(1, len(a)):
        val = a[i]
        j = i-1
        while j>=0 and val < a[j]:
            a[j+1] = a[j]
            j-=1
        a[j+1] = val
    return a

arr = [20,40,10,50,30]
print(insertion(arr))