"""
https://leetcode.com/problems/fizz-buzz/
"""
def fizzBuzz(n: int):
    i = 1
    answer = []
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
        i+=1
    return answer

n = 15
print(fizzBuzz(15))

