from Learning.DSA.Heap.BinaryHeap import operation


def countMeetings(firstDay, lastDay):
    meeting_set = set()
    counter = 0
    meet = []
    meet = list(zip(firstDay, lastDay))
    sorted_meet = sorted(meet, key= lambda x: x[1])
    print(f"sorted_meet={sorted_meet}")
    for s, e in sorted_meet:
        for i in range(s, e + 1):
            if i not in meeting_set:
                meeting_set.add(i)
                counter += 1
                break
    return len(meeting_set)

s1 = [1,2,3,3,3]
s2 = [2,2,3,4,4]

print(countMeetings(s1, s2))

errors = [500, 501, 502, 503, 504]
f = open(access0)
lines = f.read().splitlines()
res = []
from collections import Counter
tmp = []
for line in lines:
    if line[1] in errors and line[2] != "127.0.0.1":
        tmp.append(line[1])
        res.append(line)
final = []
count = Counter(tmp)[5]
for i in res:
    if count.keys() in i[1]:
        final.append(i)

f = ""


filename = "/tmp/report.log"
f = open(filename, "w")
for line in res:
    f.write(line)