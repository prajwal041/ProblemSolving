class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        digits_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        def backtrack(index, cur_comb):
            if index == len(digits):
                result.append(''.join(cur_comb))
                return

            current_digit = digits[index]
            for letter in digits_to_letters[current_digit]:
                cur_comb.append(letter)
                backtrack(index+1, cur_comb)
                cur_comb.pop()
        backtrack(0, [])
        return result

digits = "34"
s  = Solution()
print(s.letterCombinations(digits))