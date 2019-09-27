'''
Input:
4   ---> n
2   ---> a[]
1
2
2   ---> b[]
3
4

Output: 7
Explanation: (1), (1,2), (2), (2,3), (3,4), (4)


Algo:
- Get all combination in a[]
- a[-1] & b[0] ---> So +1
- missing no combining a[] & b[]
- Get all combination in a[]
'''
from itertools import combinations
def find_missing(lst,last):
    return [x for x in range(lst[0], last+1) if x not in lst]

def AngryAnimals(n,a,b):
    total = 0

    miss_a = find_missing(a, a[-1])
    miss_b = find_missing(b, n)
    #print(miss_a)
    #print(miss_b)
    miss_a_count = 0
    if len(miss_a)!=0:
        miss_list_a = a + miss_a
        comb_miss_a = combinations(list(set(miss_list_a)), 2)
        for i in list(comb_miss_a):
            miss_a_count += 1
        miss_a_count += 1  # for len of combinations
        total += len(miss_list_a) + miss_a_count
    else:
        comb1 = combinations(list(set(a)), 2)
        for i in list(comb1):
            print(i)
            miss_a_count += 1
        total += len(a) + miss_a_count

    miss_b_count = 0
    if len(miss_b) != 0:
        miss_list_b = b + miss_b
        print(miss_list_b)
        comb_miss_b = combinations(list(set(miss_list_b)), 2)
        for i in list(comb_miss_b):
            print(i)
            miss_b_count += 1
        miss_b_count += 2  # for len of combinations
        total += len(miss_list_b) + miss_b_count - len(b) + 1
    else:
        comb2 = combinations(list(set(b)), 2)
        for i in list(comb2):
            print(i)
            miss_b_count += 1
        total += len(b) + miss_b_count

    total += 1
    # total += len(a) + len(b) + miss_a_count + miss_b_count + 1
    return total

n = 5
a = [1,2]
b = [3,5]
print(AngryAnimals(n,a,b))
# lst = [2,4,5,8]
# print(find_missing(lst,lst[-1]))