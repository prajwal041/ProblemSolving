def check(s):
    for i in range(len(s) - 2):
        if s[i]=="z" and s[i+1]=="a":
            continue
        elif s[i]=="a" and s[i+1]=="z":
            continue
        if abs(ord(s[i]) - ord(s[i + 1])) != 1:
            return "NO"
    return "YES"


s = "zza"
print(check(s))