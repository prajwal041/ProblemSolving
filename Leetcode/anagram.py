s = "rat"
t = "car"
s = sorted(s)
t = sorted(t)

def anagram(s,t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

print(anagram(s,t))