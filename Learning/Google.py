def foo(a):
    for y in range(4):
        for x in range(4):
            if x+1 == len(a[0]):
                if a[0][y] != None:
                    if a[x][y] is not None:
                        a[0][y] = a[x][y]*2
                        a[0][y] = None
                if a[x][y]==None:
                    a[x][y]=a[0][y]
                    a[0][y]=None
            elif a[x+1][y]!=None:
                if a[x+1][y]==a[x][y]:
                    a[x][y]=a[x][y]*2
                    a[x+1][y]=None
                if a[x][y]==None:
                    a[x][y]=a[x+1][y]
                    a[x+1][y]=None
    return a


arr = [[4,2,4,2],[4,None,4,2],[2,None,8,2],[16,None,4,None]]
arr1 = [[2, None, 2, None], 
 [2, None, 2, None], 
 [None, None, None, None], 
 [None, None, None, None]]
print(foo(arr1))