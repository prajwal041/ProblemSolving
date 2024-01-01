def characterReplacement(s: str, k: int) -> int:
    count = {}
    l, res = 0, 0
    for r in range(len(s)):
        count[s[r]] = 1 + count