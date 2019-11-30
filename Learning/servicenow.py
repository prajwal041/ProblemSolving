def final(a):
    sums = 0
    out = []
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i]>=a[j]:
                sums+=(a[i]-a[j])
                break
            if j >= len(a)-1:
                sums+=a[i]
                out.append(i)
    sums+=a[-1]
    out.append(len(a)-1)
    print(sums)
    for i in out:
        print(i, end=" ")

arr = [5,1,3,4,6,2]
final(arr)