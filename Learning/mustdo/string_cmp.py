def string_cmp(s1,s2):
    # if s1.lower()==s2.lower():
    #     return True
    # else:
    #     return False
    if len(s1)!=len(s2):
        return False
    for i in range(len(s1)):
        if s1[i].lower()!=s2[i].lower():
            return False
    return True


def ins_del(s1, s2):
    flag = 0
    p = s2.lower()
    for i in range(len(s1)):
        if s1[i].lower() in p:
            flag = 1
    if flag == 1:
        return True
    else:
        return False


print(ins_del("abc", "ABCD"))
print(ins_del("abc", "AC"))

print(string_cmp("abc", 'ABC'))
print(string_cmp("abc", "def"))
