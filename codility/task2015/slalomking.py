def LongestIncreasingSubsequence(seq):
    sval = [None]* (len(seq)+1)
    sval[0]=-1
    slength = 0
    for i in range(len(seq)):
        lower = 0
        upper = slength
        while lower<=upper:
            mid = (lower+upper)//2
            if seq[i] < sval[mid]:
                upper=mid-1
            elif seq[i]>sval[mid]:
                lower=mid+1
            else:
                return 0
        if sval[lower]==None:
            sval[lower]=seq[i]
            slength+=1
        else:
            sval[lower]=min(sval[lower], seq[i])

    return slength

def solution(a):
    bound = max(a)+1
    li = []
    for i in a:
        li.append(bound*2+i)
        li.append(bound*2-i)
        li.append(i)
    return LongestIncreasingSubsequence(li)

a = [15,13,5,7,4,10,12,8,2,11,6,9,3]
print(solution(a))