from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        d = Counter(tasks)
        res = []
        while len(d) > 0:
            min_val = min(d.values())
            min_key = self.get_min_key(d, min_val)
            if min_key in res:
                for _ in range(n-1):
                    res.append("Idle")

            res.append(min_key)
            d[min_key] = min_val-1
            if d[min_key] == 0:
                del d[min_key]
            print(d, res)
        print(len(res))

    def get_min_key(self, d, val):
        return list(d.keys())[list(d.values()).index(val)]

tasks = ["A","A","A","B","B","B"]
n = 3
s = Solution()
s.leastInterval(tasks, n)