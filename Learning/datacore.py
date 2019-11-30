# def grading(v):
#     k = 0
#     for i in v:
#         if i == 1:
#             k+=1
#         else:
#             break
#     return k-1

def grading(v):
    k = 0
    d = {}
    for i in range(len(v)):
        if v[i] == 1:
            k+=1
        else:
            k-=1

        d[i] = k
    print(d)
    val = max(d.values())
    return(list(d.keys())[list(d.values()).index(val)])

v = [0,1,1,0,0,1,1,1,1,1]
print(grading(v))