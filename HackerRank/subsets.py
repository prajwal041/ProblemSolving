s = input()
def subset(s):
    if s == []:
        return (s)
    sets = [s]
    for i in range(0, len(s)):
        t_subset = subset(s[:i]+s[i+1:])
        for subset in t_subset:
            if subset not in sets:
                sets.append(subset)
    return sets


print(subset(s))