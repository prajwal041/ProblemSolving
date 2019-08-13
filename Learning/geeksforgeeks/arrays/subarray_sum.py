def getsum(n,s,a):
    sums = a[0]
    start = 0
    i = 1
    while i<=n:
        while sums>s and start<i-1:
            sums-=a[start]
            start+=1
        if sums == s:
            return(start+1,i)
        if i<=n:
            sums+=a[i]
        i+=1
    return 0

a = [1,2,3,5,7]
s = 12
n = len(a)
print(getsum(n,s,a))