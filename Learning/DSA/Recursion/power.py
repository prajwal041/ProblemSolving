def power(a,b):
     if a==0 or b==1:
         return a
     elif b==1:
         return a
     else:
         return a*power(a,b-1)

a,b = 2,7
print(power(a,b))