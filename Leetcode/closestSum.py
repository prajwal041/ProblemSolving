

def closestSum(l1, l2, target):
    l1_sorted = sorted(l1)
    l2_sorted = sorted(l2)
    i = 0
    j = len(l2_sorted) - 1
    small_diff = abs(l1_sorted[0] + l2_sorted[0] - target)
    close_pair = (l1_sorted[0], l2_sorted[0])
    while i < len(l1_sorted) and j>=0:
        v1 = l1_sorted[i]
        v2 = l2_sorted[j]
        current_diff = v1 + v2 - target
        if abs(current_diff) < small_diff:
            small_diff = abs(current_diff)
            close_pair = (v1, v2)
        if current_diff == 0:
            return close_pair
        elif current_diff < 0:
            i+=1
        else:
            j-=1
    return close_pair


arr1 = [7,4,1,10]
arr2 = [4,5,8,7]
target = 13
print(closestSum(arr1, arr2, target))
