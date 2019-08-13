newconstruct = [[1,2,5], [1,3,10],[1,6,2],[5,6,5]]
pending = [[1,2],[5,6],[1,6],[3,6]]
pending.remove([3,6])
# print(pending)
# print(newconstruct[0][2])
li = []
min = newconstruct[0][2]
for i in range(len(newconstruct)):
    if newconstruct[i][2]< min:
        min = newconstruct[i][2]
        li = newconstruct[i]
print(min)
min1 = 0
li.remove(min)
print(li)
if li == [1,6]:
    min1 = newconstruct[0][2]
cost = min+ min1
print(cost)