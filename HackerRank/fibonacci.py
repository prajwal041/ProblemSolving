def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(i+1,"a:",a)
        a,b = b,a+b
    return(a)
n = int(input())
print(fibonacci(n))

'''
Time complexicity T ~ O(n)

Input:
3

Output:
2
'''