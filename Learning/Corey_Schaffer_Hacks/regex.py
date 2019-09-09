# import re
#
# text = '''
# 123-456-7895
# 123.456.7895
# '''
# pat = re.compile(r'(\d\d\d)(-|\.)(\d\d\d)(-|\.)(\d\d\d\d)')
# mat= pat.finditer(text)
# for i in mat:
#     print(i)

def is_perm_matrix(m):
    #Check rows
    if all(sum(row) == 1 for row in m):
        #Check columns
        return all(sum(col) == 1 for col in zip(*m))
    return False

m1 = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
]

val = is_perm_matrix(m1)
if val == False:
    print(0)
else:
    print(1)


# b[i]=bin(int(a[i]))[2:].zfill(8)
# print(bin(b).zfill(3))
a = [0,1,2]
b=[]
# for i in range(len(a)):
#     b.append(list(bin(int(a[i]))[2:].zfill(3)))

for i in range(len(a)):
    b.append([int(numeric_string) for numeric_string in list(bin(int(a[i]))[2:].zfill(3))])
print(b)