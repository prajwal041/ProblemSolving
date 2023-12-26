def groupAnagram(strs):
    from collections import defaultdict
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c)-ord("a")]+=1
        print(f"count={count}")
        res[tuple(count)].append(s)
        print(f"res={res}")
    return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagram(strs)

'''
Time ~ O(m* n)
Space = O(m)
'''
