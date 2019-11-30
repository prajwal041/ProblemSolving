from collections import defaultdict

def longpalindrome(s):
    ind_ch = defaultdict(list)
    for ind,ch in enumerate(s):
        ind_ch[ch].append(ind)

    max_pal_l = 0
    max_pal= ""
    for ind,ch in enumerate(s):
        key_indices = [ i for i in ind_ch[ch] if i>=ind]
        for key in key_indices:
            substring = s[ind:key+1]
            if substring == substring[::-1]:
                if max_pal_l < key+1-ind:
                    max_pal_l = key+1-ind
                    max_pal = substring
        if len(s)+1-ind>max_pal_l:
            break
    return max_pal

s = "malayalamask"
print(longpalindrome(s))