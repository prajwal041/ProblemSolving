def kadane(arr,n):
    fmax = 0
    tmax = 0
    for i in arr:
        tmax+=i
        if tmax < 0:
            tmax = 0
        if fmax < tmax:
            fmax = tmax
    if fmax == 0:
        if n == 1:
            return arr[0]
        return -1
    return fmax

p = int(input())

for _ in range(p):
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    print(kadane(arr, n))

# def do_one():
#     _ = input()
#     arr = [int(x) for x in input().split()]
#     for i, e in enumerate(arr):
#         if not i:
#             continue
#         arr[i] = max(e, arr[i - 1] + e)
#     print(max(arr))
#
#
# for _ in range(int(input())):
#     do_one()
#
# def kadane_sum(arr, n):
#     max_so_far = 0
#     max_ending_here = 0
#     for ele in arr:
#         max_ending_here += ele
#         if max_so_far < max_ending_here:
#             max_so_far = max_ending_here
#         if max_ending_here < 0:
#             max_ending_here = 0
#     if max_so_far == 0:
#         if n == 1:
#             return arr[0]
#         return -1
#     return max_so_far
#
# tc = int(input())
# for _ in range(tc):
#     n = int(input())
#     arr = list(map(int, input().strip().split(' ')))
#     print(kadane_sum(arr, n))

