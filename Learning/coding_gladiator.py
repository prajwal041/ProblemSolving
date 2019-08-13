''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def winlose(num):
    li1 =list(input())
    li2 =list(input())
    for i in range(int(num)):
        if li1[i]>li2[i]:
            return "WIN"
    return "LOSE"
 # Write code here


n = int(input())
for _ in range(0,n):
    num = input()
    print(winlose(num))
