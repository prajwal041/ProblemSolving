def closest_sum_pair(l1,l2,target):
    l1_sort = sorted(l1)
    l2_sort = sorted(l2)
    i = 0
    j = len(l2_sort)-1
    small_diff = abs(l1_sort[0]+l2_sort[0]-target)
    closest_pair = (l1_sort[0],l2_sort[0])
    while i < len(l1_sort) and j >=0:
        v1 = l1_sort[i]
        v2 = l2_sort[j]
        current_diff = v1 + v2 -target
        if abs(current_diff)<small_diff:
            small_diff = abs(current_diff)
            closest_pair = (v1, v2)
        if current_diff == 0:
            return closest_pair
        elif current_diff < 0:              # checking rows & columns
            i+=1
        else:
            j-=1
    return closest_pair

l1 = [1,5,7,2]
l2 = [10,4,6,11]
target = 14
print(closest_sum_pair(l1,l2,target))