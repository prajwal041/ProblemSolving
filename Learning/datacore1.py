def fountain(s):
    fount =0
    i=0
    while i < len(s):
        if s[i]!=0:
            start = s[i] - i
            if start <0:
                start = 0
            end = s[i] + i
            if end > len(s):
                end = len(s)
            i = end
            for j in range(start, end):
                fount =1
        else:
            fount+=1
            i+=1
    return fount


s =[2,0,0,0]
print(fountain(s))