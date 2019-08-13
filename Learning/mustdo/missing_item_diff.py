
# s = "ABcd"
# # n = len(s)-1
# # c = []
# # while n>=0:
# #     c.append(s[n])
# #     n-=1
# # print("".join(c))

def missing(l1,l2):
    n1 = len(l1)
    n2 = len(l2)
    l1 = set(l1)
    l2 = set(l2)
    if n1>n2:
        return l1.difference(l2)
    else:
        return l2.difference(l1)

def missing1(l1,l2):
    xsum = 0
    for num in l1:
        xsum ^=num
    for num in l2:
        xsum ^=num
    return xsum

l1 = [1,2,3,4]
l2 = [1,4]
print(missing1(l1,l2))