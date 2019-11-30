s = "I am using HackerRank to improve programming"
t = "am HackerRank to improve"
import re
s = set(re.split(' |,-',s))
t = set(re.split(' |,-',t))
print(sorted(s.difference(t)))
