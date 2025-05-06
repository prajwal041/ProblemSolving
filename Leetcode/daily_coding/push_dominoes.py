
class Solution:
    def pushDominoes(self, dominoes):
        dominoes = "L" + dominoes + "R"
        res = []
        i = 0
        for j in range(1, len(dominoes)):
            if dominoes[j] == ".":
                continue

            mid = j - i - 1
            if i > 0:
                res.append(dominoes[i])

            if dominoes[i] == dominoes[j]:
                res.append(dominoes[i] * mid)
            elif dominoes[i] == "L" and dominoes[j] == "R":
                res.append('.' * mid)
            else:
                half = mid // 2
                res.append('R' * half)
                if mid % 2 == 1:
                    res.append('.')
                res.append('L' * half)

            i = j
        return ''.join(res)

dominoes = ".L.R...LR..L.."
s = Solution()
print(s.pushDominoes(dominoes))

