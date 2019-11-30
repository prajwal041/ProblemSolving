def check_panagrams(strings):
    result = ""
    for s in strings:
        inp = set(s.lower())
        alpha = [ch for ch in inp if ord(ch) in range(ord('a'), ord('z')+1)]
        if len(alpha)==26:
            result+='1'
        else:
            result+='0'
    return result

strings = []
n = int(input())
for _ in range(n):
    strings.append(input())
print(check_panagrams(strings))