def checkInclusion(s1, s2):
    from collections import Counter
    l, r = 0, len(s2) - 1
    k = 0
    s1_hash = Counter(s1)
    if s1 == s2 or s1[::-1] == s2 or s1 == s2[::-1]:
        return True
    keys = s1_hash.keys()
    len_keys = len(keys) * [0]
    s2_hash = dict(zip(keys, len_keys))
    while l < r:
        cur = s2[l]
        if s2[l] in s2_hash.keys():
            k += 1
            s2_hash[s2[l]] += 1
            if s1_hash == s2_hash and k == len(s1):
                return True
            else:
                s2_hash[s2[l]] -= 1
        else:
            k = 0
        l += 1
    return False
def inclusion(s1, s2):
    from collections import Counter
    l, r = 0, len(s2) - 1
    if s1 == s2 or s1[::-1] == s2 or s1 == s2[::-1]:
        return True
    len_s1 = len(s1)
    s1_hash = Counter(s1)
    while l < r:
        cur = s2[l]
        s2_hash = Counter(s2[l:len_s1])
        if s1_hash == s2_hash:
            return True

        l+=1
        len_s1 +=1
    return False
s1 = "ab"#"hello"
s2 = "eidbaooo"
print(inclusion(s1, s2))