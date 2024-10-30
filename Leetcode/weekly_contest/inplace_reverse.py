def inplace_reverse(s):
    left, right = 0, len(s) - 1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

if __name__ == '__main__':
    s = [0,1,2,3]
    print(inplace_reverse(s))