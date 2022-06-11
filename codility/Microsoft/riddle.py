class Solution:
    def modifyString(self, s: str) -> str:
        s, N = list(s), len(s)

        def what_to_avoid(i):
            avoid = set()
            if i > 0: avoid.add(s[i - 1])
            if i + 1 < N: avoid.add(s[i + 1])
            return avoid

        for i in range(N):
            if s[i] == '?':
                avoid = what_to_avoid(i)
                if 'a' not in avoid:
                    s[i] = 'a'
                elif 'b' not in avoid:
                    s[i] = 'b'
                else:
                    s[i] = 'c'

        return ''.join(s)

string = "????????"
s = Solution()
print(s.modifyString(string))