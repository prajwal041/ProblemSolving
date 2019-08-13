def solution(a):
    disc_count = len(a)
    range_upper = [0]*disc_count
    range_lower = [0]*disc_count
    for i in range(disc_count):
        range_upper[i]=i+a[i]
        range_lower[i]=i-a[i]
    range_upper.sort()
    range_lower.sort()
    range_lower_index=0
    intersect_count = 0
    for range_upper_index in range(disc_count):
        while range_lower_index<disc_count and range_upper[range_upper_index]>=range_lower[range_lower_index]:
            range_lower_index+=1
        intersect_count+=range_lower_index-range_upper_index-1
        if intersect_count>10000000:
            return -1
    return intersect_count

a = [1,5,2,1,4,0]
print(solution(a))
