def titleno(s):
    s = s.upper()
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    maps = {}
    for i in range(26):
        maps[LETTERS[i]] = i + 1

    col = 0
    for l in s:
        col = 26 * col + maps[l]

    return col

print(titleno('AB'))