from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        d = Counter(tasks)

        # Sort the frequencies in descending order
        freq = sorted(d.values(), reverse=True)

        # max frequency
        max_freq = freq[0]

        # Calculate the maximum possible idle time
        idle_time = (max_freq-1) * n

        # Reduce idle time based on the remaining tasks
        for f in freq[1:]:
            idle_time -= min(max_freq-1, f)
            print(f"idle_time: {idle_time}")

        # Idle time can't be negative
        idle_time = max(0, idle_time)

        return len(tasks) + idle_time

    def get_min_key(self, d, val):
        return list(d.keys())[list(d.values()).index(val)]

tasks = ["A","A","A","B","B","B"]
n = 2
s = Solution()
print(s.leastInterval(tasks, n))