# Example 1:
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
import re
def GCD(str1,str2):
    for i in range(len(str2)):
        if str2[i] in str1:
            str1 = re.sub(str2[i].index(str2[i]),'',str1)
            # print(str2[i])
            # str1.replace(str2[i].index(str2[i]),'')
    return str1

    # str1 = [word for word in str1]
#     # str2 = [word for word in str2]
#     #
#     # str1 = set(str1)
#     # str2 = set(str2)
#     # print(str1)
#     # result = str1.difference(str2)
#     # print(result)
#     # result=" ".join(result)
#     # return result

print(GCD("ABCABC","ABC"))


