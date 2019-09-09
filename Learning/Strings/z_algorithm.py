def search_without_sentinel(pattern, text):
    """Search without the sentinel."""
    s = pattern + text
    Z = [0] * len(s)
    Z[0] = len(s)

    rt = 0
    lt = 0

    occurrence = []

    for k in range(1, len(s)):
        if k > rt:
            n = 0
            while n + k < len(s) and s[n] == s[n + k]:
                n += 1
            Z[k] = n
            if n > 0:
                lt = k
                rt = k + n - 1
        else:
            p = k - lt
            right_part_len = rt - k + 1

            if Z[p] < right_part_len:
                Z[k] = Z[p]
            else:
                i = rt + 1
                while i < len(s) and s[i] == s[i - k]:
                    i += 1
                Z[k] = i - k

                lt = k
                rt = i - 1

        Z[k] = min(len(pattern), Z[k])

        # An occurence found.
        if Z[k] == len(pattern):
            occurrence.append(k - len(pattern))

    return occurrence

string = "abcxxxabyyy"
pattern = "ab"
print(search_without_sentinel(pattern,string))