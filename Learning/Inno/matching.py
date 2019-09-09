from difflib import SequenceMatcher


def longestSubstring(str1, str2):
    # initialize SequenceMatcher object with
    # input string
    seqMatch = SequenceMatcher(None, str1, str2)

    # find match of longest sub-string
    # output will be like Match(a=0, b=0, size=5)
    match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))
    return str1[match.a: match.a + match.size]
    # print longest substring
    # if (match.size != 0):
    #     print(str1[match.a: match.a + match.size])
    # else:
    #     print('No longest common sub-string found')


str = 'ab'
pre = 'b'
suf = 'a'
val1 = longestSubstring(str,pre)
val2 = longestSubstring(str,suf)
print(val1)
print(val2)
if str.index(val1)>str.index(val2):
    print(val2)
print(str[str.index(val1[:1]):len(str)-str[::-1].index(val2[-1])])
