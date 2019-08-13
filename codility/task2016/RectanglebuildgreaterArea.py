def solution(a,x):
    if a.count(x)<2:
        return 0
    d = {}
    count = 0
    for i in a:
        d[i] = a.count(i)
        
    for i in d:
        if d.get(i) >= 2 and i!=x:
            count+=1
            # print(d.get(i),i)
            # print(list(d.keys())[list(d.values()).index(d.get(i))])
    return count


a = [1,2,5,1,1,2,3,5,1]
print(solution(a,5))