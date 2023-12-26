from collections import Counter

def containsDuplicate(nums):
    hash = Counter(nums)
    print(hash.values())
    for item in hash.values():
        if item > 1:
            return True
    return False

nums = [1,2,3,4]
print(containsDuplicate(nums))