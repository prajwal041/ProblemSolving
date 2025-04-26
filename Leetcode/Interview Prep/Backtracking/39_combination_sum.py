from itertools import combinations
class Solutions:
    def combinationSum(self, candidates, target):
        res = []
        for i in range(len(candidates)):
            for j in list(combinations(candidates, i)):
                print((list(j)))
                if sum(list(j)) == target:
                    res.append(list(j))
        return res

candidates = [2,3,6,7]
target = 7
s = Solutions()
print(s.combinationSum(candidates, target))