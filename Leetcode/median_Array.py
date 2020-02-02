def merge_median(l1, l2):
    from heapq import merge
    merge_list = l1+l2
    if len(merge_list)%2!=0:
        return merge_list[int(len(merge_list))//2]
    else:
        median1 = int(len(merge_list)//2)
        median2 = int(len(merge_list)-1)//2
        return (merge_list[median1] + merge_list[median2])/2

l1 = [1.0,2.0]
l2 = [3.0,4.0]
print(merge_median(l1, l2))