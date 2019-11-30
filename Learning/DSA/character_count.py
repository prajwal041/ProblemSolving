from collections import Counter
def char_count(s):
    if len(s) == 0:
        return 0
    return Counter(s)

s = input()
print(char_count(s))

d= {'A': 10, 'B': 20}
print(list(d.keys())[list(d.values()).index(10)])