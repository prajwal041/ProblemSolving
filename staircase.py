(lambda num: [print(('#'*x).rjust(num)) for x in range(num+1)])(int(input().strip()))

n = input()
print("\n".join([" "*(n-x)+"#"*(x) for x in range(1,n+1)]))