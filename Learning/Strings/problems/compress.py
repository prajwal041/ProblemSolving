def compress(s):
    count = 1
    output = s[0]
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count +=1
        else:
            if count >1:
                output+=str(count)
            output+=s[i+1]
            count = 1
    if count > 1:
        output+=str(count)
    return output

s = "mississippi"

print(compress(s))