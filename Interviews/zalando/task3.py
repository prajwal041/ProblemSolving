a = [2,1,3,5,4]
d = []
c = 0
def checkConsecutive(l):
    if len(l)!=0:
        return sorted(l) == list(range(min(l), max(l) + 1))

for i in a:
    if i==1:
        c+=1
    elif checkConsecutive(d)==True and 1 in d:
        c+=1
    d.append(i)
print(c)
print(d)