'''
Input:
1
aaaabbaa

Output:
aabbaa
'''


class Solution:
    def longestPalindrome(self, s):
        from collections import defaultdict
        index_dict = defaultdict(list)
        # Construct indices dictionary for all characters - o(n) Run time and o(n) storage
        for i, c in enumerate(s):
            index_dict[c].append(i)

        max_palindrome = ''
        max_palindrome_l = 0

        # Loop through all characters in string
        for ind, ch in enumerate(s):
            # Get indices which are greater than the current character from index_dict
            key_indices = [i for i in index_dict[ch] if i >= ind]
            # Loop through the other indices of the character in reversed order
            for key in sorted(key_indices, reverse=True):
                substring = s[ind:key + 1]
                # If the substring is a palindrome
                if substring == substring[::-1]:
                    # Check whether length is greater than existing palindrome
                    if max_palindrome_l < (key + 1 - ind):
                        max_palindrome_l = (key + 1 - ind)
                        max_palindrome = substring
                    # If length of palindrome already found is greater than remaing characters, stop the loop
            if (len(s) + 1 - ind) < max_palindrome_l:
                break
        return max_palindrome

s = "aaaabbaa"
sol = Solution()
print(sol.longestPalindrome(s))
