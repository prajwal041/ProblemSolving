def solution(a):
    d = {}
    for i in a:
        d[i] = a.count(i)

    for i in d.values():
        if i%2!=0:
            return list(d.keys())[list(d.values()).index(i)]
    #     if i%2!=0:
    #         return list(d.keys())[list(d.values()).index(i)]

def solutionA(a):
    result =0
    for i in a:
        result = result^i
    return result
a = [9,3,9,3,9,7,9]
print(solutionA(a))



