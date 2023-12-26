def isAnagram(s, t):
    if len(s) != len(t):
        return False
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    item = 0
    while item < len(s):
        if sorted_s[item] != sorted_t[item]:
            return False
        item+=1
    return True

s = "rat"
t = "car"
print(isAnagram(s, t))
