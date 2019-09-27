s = "abcabccb"

def subs(s):
    d = ""
    f = ""
    for i in range(len(s)):
        if s[i] not in s:
            f += s[i]
        else:
            if len(d) < len(f):
                d = f
            f = f[f.index(s[i])+1::] + s[i]
    return max(len(d), len(f))
print(subs(s))



# d = ""
# f = ""
# for i in range(len(s)):
#     if s[i] not in f:
#         f += s[i]
#     else:
#         if len(d) < len(f):
#             d = f
#         f = f[f.index(s[i]) + 1::] + s[i]
#
# print(max(len(d), len(f)))