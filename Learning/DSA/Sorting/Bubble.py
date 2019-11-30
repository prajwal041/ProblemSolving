def bubble(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]> a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

arr = [100,20,30,10,50,70,60,80,90]
print(bubble(arr))
