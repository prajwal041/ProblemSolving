def stockplan(s,p):
    p[0]=1
    for i in range(1, len(s)):
        p[i]=1
        if s[i] < s[i-1]:
            p[i]=1

        else:
            j = i-1
            while j>=0 and s[i]>=s[j]:
                p[i]+=1
                j-=1
    print(p)

arr = [10, 4, 5, 90, 120, 80]
p = [0] * len(arr)
stockplan(arr,p)