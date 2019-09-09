vowels = ['a', 'e', 'i', 'o', 'u']

# Mapping values for vowels
mapping = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}


# Function to check if given subsequence
# contains all the vowels or not
def isValidSequence(subList):
    for vowel in vowels:
        if vowel not in subList:
            return False

    return True


def longestSubsequence(string, subList, index):
    def helper(chosen="", i=0):
        if i == len(string):
            return chosen if set("aeiou").issubset(set(chosen)) else ""

        hashable = (chosen[-1] if chosen else None, len(chosen), i)

        if hashable in memo:
            return memo[hashable]

        if not chosen:
            res = helper("a" if string[i] == "a" else chosen, i + 1)
        elif chosen[-1] == string[i]:
            res = helper(chosen + string[i], i + 1)
        elif mapping[chosen[-1]] + 1 == mapping[string[i]]:
            sub1 = helper(chosen + string[i], i + 1)
            sub2 = helper(chosen, i + 1)

            res = sub1 if len(sub1) > len(sub2) else sub2
        else:
            res = helper(chosen, i + 1)

        memo[hashable] = res
        return res

    mapping = {x: i for i, x in enumerate("aeiou")}
    memo = {}
    return helper()


string = "aeiaaioooauuaeiou"

subsequence = longestSubsequence(string, [], 0)
if len(subsequence) == 0:
    print("No subsequence possible")
else:
    print(len(subsequence))