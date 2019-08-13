'''
Problem: Python Reverse arguments
https://www.hackerrank.com/tests/66g0bossg4s/questions/fnhe60rm56f

Input:
4
pow 2 3
cmp 1 2
join_with coder best the are you ,
capitalize_first_and_join first second third

Output:
9
1
you,are,the,best,coder
THIRDsecondfirst

Time T ~ O(n), where n is the number of queries
'''
from functools import wraps
def reversed_args(f):
    @wraps(f)
    def newfunc(*args):
        return f(*args[::-1])
    return newfunc

int_func_map = {
    'pow': pow,
    'cmp': lambda a,b: 0 if a == b else [1,-1][a<b],
}
string_func_map = {
    'join_with': lambda separator, *args: separator.join(args),
    'capitalize_first_and_join': lambda first, *args: ''.join([first.upper()] + list(args)),
}

queries = int(input())
for i in range(queries):
    line = input().split()
    func_name, args = line[0], line[1:]
    # args = args[::-1]

    if func_name in int_func_map:
        args = list(map(int, args))
        print(reversed_args(int_func_map[func_name])(*args))
    else:
        print(reversed_args(string_func_map[func_name])(*args))
