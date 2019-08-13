s = "Let's take LeetCode contest"
string = s.split()
result = ""
for i in string:
    result+=i[::-1]
    result+=" "
print(result[:-1])