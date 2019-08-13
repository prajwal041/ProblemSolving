import re
s = "2[bc]a"
def comp_decomp(s):
   stack = []
   result = ""
   ops = ""
   digit = 1
   for i in s:
       if i.isdigit():
           digit = int(i)
       if i == "[":
           stack.append(i)
       if i == "]":
           stack.pop()
           result += ops * digit
       if len(stack)==0:
           result+=i
           ops = ""
       else:
           ops = ops +i
   result = re.sub(r'[\[\]]','',result)
   result = re.sub(r'[0-9]','',result)
   return result

print(comp_decomp(s))
