
open_list = ["(", "[", "{"]
close_list = [")", "]", "}"]

def bracket_check(s):
    stack = []
    for i in s:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(stack)>0 and open_list[pos]==stack[len(stack)-1]:
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack)==0:
        return "Balanced"
    else:
        return "UnBalanced"

s = "()("
# count = bracket_check(s)
# if count == 0:
#     print("Balanced string")
# else:
#     print(count)
print(bracket_check(s))