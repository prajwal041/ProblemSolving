'''
Largest contigeous subarray
'''
def kadane(arr,n):
    fmax = 0
    tmax = 0
    s = 0
    start = 0
    end = 0
    for i in range(len(arr)):
        tmax+=arr[i]
        if tmax < 0:
            tmax = 0
            s = i+1
        if fmax < tmax:
            fmax = tmax
            start = s
            end = i
    if fmax == 0:
        if n == 1:
            return arr[0]
        return -1
    return fmax,start,end

arr = [2,-2,4,5,8,-9]
n = len(arr)

sums,start,end = kadane(arr,n)
print(sums)
print(arr[start:end+1])

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

