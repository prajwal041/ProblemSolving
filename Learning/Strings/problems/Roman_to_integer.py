def roman(no):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = len(no)
    total = d[no[n-1]]
    for i in range(n-1,0,-1):
        current = d[no[i]]
        prev = d[no[i-1]]
        if prev>=current:
            total+=prev
        else:
            total-=prev

    return total

n = int(input())
for _ in range(n):
    no = input()
    print(roman(no))