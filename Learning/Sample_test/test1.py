li1 = [1,3,4,5,6]
li2 = [2,4,5,8,9,10]
'''
unique of li 1
unique of li 2
common of l1 & li2

'''
def resultant(li1, li2):
    common = []
    result1 = []
    for i in li1:
        if i in li2:
            common.append(i)
        else:
            result1.append(i)

    result2 = []
    for i in li2:
        if i not in li1:
            result2.append(i)
    return common, result1, result2
commons, unique1, unique2 = resultant(li1, li2)
print(f'commons={commons}, unique elements in li1={unique1}, unique elements in li2={unique2}')
