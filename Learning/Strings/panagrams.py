def checkPangram(strings):
    # Write your code here
    li = ""
    for s in strings:
        input = s.lower()

    # convert input string into Set() so that we will
    # list of all unique characters present in sentence
        input = set(input)

    # separate out all alphabets
    # ord(ch) returns ascii value of of character
        alpha = [ch for ch in input if ord(ch) in range(ord('a'), ord('z') + 1)]

        if len(alpha) == 26:
            li = li + '1'
        else:
            li = li + '0'
    return li


strings_count = int(input().strip())

strings = []

for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

result = checkPangram(strings)
print(result)