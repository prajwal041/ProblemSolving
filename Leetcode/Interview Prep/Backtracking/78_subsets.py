from itertools import combinations

class Solutions:
    def subsets(self, nums):
        res = set()
        for i in range(len(nums)):
            for item in list(combinations(nums, i)):
                res.add(item)
        output = [list(x) for x in res]
        output.append(nums)
        return output

nums = [1,2,3]
s = Solutions()
print(s.subsets(nums))

