def minimum(li):
    sum = 0
    while(len(li)>=2):
        li = sorted(li)
        l1 = li[0]
        l2 = li[1]
        del li[:2]
        s = l1+l2
        sum += s
        li.append(s)
        print(sum)
        print(li)
    return sum

n = input()
# li = list(map(int, input().split()))
li = [8,4,6,12]
r = minimum(li)
print(r)