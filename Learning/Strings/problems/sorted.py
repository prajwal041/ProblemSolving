from collections import defaultdict

t = int(input())
while t > 0:
    t -= 1
    s = input()
    data = defaultdict(int)
    for ch in s:
        data[ch] += 1
    print(''.join(map(lambda x: x[0] * x[1], sorted(data.items(), key=lambda x: x[::-1]))))