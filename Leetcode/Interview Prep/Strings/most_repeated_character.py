def most_repeated_character(s):
    from collections import Counter
    '''
    Solution 1
    d = dict()
    for item in s:
        if ord(item) in d.keys():
            d[ord(item)] += 1
        else:
            d[ord(item)] = 1
    max_key = chr(max(zip(d.keys(), d.values()))[0])
    '''
    # Solution 2
    count_dict = Counter(s)

    print(f"count_dict: {count_dict}")
    max_val = max(count_dict.values())
    max_key1 = list(count_dict.keys())[list(count_dict.values()).index(max_val)]
    print(f"max_key1: {max_key1}")
    #max_key = max(count_dict, key =lambda x: count_dict[x])
    max_key = max(zip(count_dict.keys(), count_dict.values()))[0]
    return max_key




s = 'abbbba123'
print(most_repeated_character(s))
'''
output: b
'''
