def longestEvenWord(s):
    # Write your code here
    # split the string
    s = s.split(' ')
    d = {}
    # iterate in words of string
    for word in s:
        # if length is even
        if len(word)%2==0:
            d[word]=len(word)
    if d=={}:
        return 00
    return max(d)
s='It is a pleasant day today'
print(longestEvenWord(s))