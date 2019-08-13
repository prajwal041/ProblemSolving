a = input()
b = input()

com = set(a).intersection(b)
anagram = sum(min(a.count(char),b.count(char)) for char in com)
print(len(a)+len(b)-2*anagram)

'''
Input:
cde
abc

Output:
4

T ~ (n)

'''