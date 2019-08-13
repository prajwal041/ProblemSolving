def is_sorted(arr):
    return True if list(arr) == sorted(arr) else False

for _ in range(int(input())):
    arr = (sorted(input()) for _ in range(int(input())))
    sorted_col = (is_sorted(z) for z in zip(*arr))
    print(['NO','YES'] [all(sorted_col)])

'''
Input:
1
5
ebacd
fghij
olmkn
trpqs
xywuv

Output:
YES

T ~ O(n)
S ~ O(1)
'''