class Solution:

    def encode(self, st):
        res = ""
        for s in st:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, st):
        res, i = [], 0

        while i < len(st):
            j = i
            while st[j] != "#":
                j +=1
            length = int(st[i:j])
            res.append(st[j+1: j+1 + length])
            i = j+1+length
        return res

"""
Time & space complexicity: O(n) , n of characters
"""

input = ["neet", "code"]
s = Solution()
encode = s.encode(input)
print(f"encode = {encode}")
decode = s.decode((encode))
print(f"decode = {decode}")