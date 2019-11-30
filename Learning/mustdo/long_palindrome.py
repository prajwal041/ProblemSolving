class LongPalindrome:
    def palindrome(self, s):
        from collections import defaultdict
        ind_dict = defaultdict(list)
        pal = ""
        pal_l = 0

        for ind,ch in enumerate(s):
            ind_dict[ch].append(ind)

        for ind, ch in enumerate(s):
            key_indices = [i for i in ind_dict[ch] if i>=ind]
            for key in sorted(key_indices, reverse=True):
                substring = s[ind:key+1]
                if substring == substring[::-1]:
                    if pal_l<key+1-ind:
                        pal_l = key+1-ind
                        pal = substring
            if len(s)+1-ind<pal_l:
                break
        return pal


s = "malayalam"
p = LongPalindrome()
print(p.palindrome(s))