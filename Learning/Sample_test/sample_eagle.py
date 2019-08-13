from collections import Counter
def missingNumbers(arr, brr):
    # for i in arr:
    #     if i in brr:
    #         brr.remove(i)
    # return brr
    a = Counter(arr)
    b = Counter(brr)
    return sorted((b-a).keys())

arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

print(missingNumbers(arr,brr))
