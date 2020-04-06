"""
Problem: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
"""
def reverse(n):
    rev = 0
    while n > 0:
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    return n

def beautifulDays(i,j,k):
    count = 0
    for p in range(i,j+1):
        if(p-int(str(p)[::-1]))%k==0:
            count += 1
    return count


if __name__ == '__main__':

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(result)


"""
Input:
20 23 6

Output:
2
"""
