import re
text = 'Glebh061@hackerrank.com'
pat = re.compile(r'^\W?[a-z]+_?[0-9]*@hackerrank.com')
if pat.search(text) is not None:
    print(True)
else:
    print(False)
mat = pat.search(text)
print(mat)
'''
^[\s]*(?:\b[A-Z]+\b[\s]*){1}(?=[:-])
'''