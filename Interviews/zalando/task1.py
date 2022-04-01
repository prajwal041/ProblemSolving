
a = [3,5,6,3,3,5]

d = {}
for i in range(len(a)):
    d[i] = a[i]
print(d)

from itertools import chain

# initialising dictionary
ini_dict = d

# printing initial_dictionary
print("initial_dictionary", str(ini_dict))

# finding duplicate values
# from dictionary using set
rev_dict = {}
for key, value in ini_dict.items():
    rev_dict.setdefault(value, set()).add(key)
c = 0
for key, values in rev_dict.items():
    if len(values)>1:
        t = list(values)
        import itertools

        for a, b in itertools.combinations(t, 2):
            if a<b:
               c+=1
print(c)



# result = set(chain.from_iterable(
#     values for key, values in rev_dict.items()
#     if len(values) > 1))

# printing result
# print("resultant key", str(result))