def closest_pair(l1,l2,target):
    l1 = sorted(l1)
    l2 = sorted(l2)
    i = 0
    j = len(l2)-1
    small_diff = l1[0]+l2[0]-target
    small_pair = (l1,l2)
    while i<len(l1) and j>=0:
        current_sum = l1[i]+l2[j]-target
        current_pair = (l1[i],l2[j])
        if current_sum<small_diff:
            current_sum = small_diff
            current_pair = (l1[i],l2[j])
        if current_sum ==0:
            return current_pair
        if current_sum<0:
            i+=1
        else:
            j-=1

l1 = [1,2,3,4,5]
l2 = [3,4,4,6,7]
target =10
print(closest_pair(l1,l2,target))

