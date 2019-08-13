'''
Problem: Check whether given lines in X-axis are overlapping or not

Algorithm Solution: 1. Check whether the point x3 lies between the line (x1,x2)
                    2. if yes then return its overlapping otherwise not
Test case 1: (x1,x2) = (1,5)
             (x3,x4) = (2,6)
Output : Overlapping
Analysis: Since x3=2 falling in the range of (1,5)

Test case 2: (x1,x2) = (1,5)
             (x3,x4) = (6,8)
Output : Not Overlapping
Analysis: Since x3=6 aren't falling in the range of (1,5)

Test case 3: (x1,x2) = (1,5)
             (x3,x4) = (5,8)
Output : Not Overlapping
Analysis: Since x3=5 aren't falling in the range of (1,5)

Time complexity:
T ~ O(1)
'''
def check_overlap(x1,x2,x3,x4):
    if x3 in range(x1, x2):
        return ("Overlapping")
    else:
        return ("Not Overlapping")


x1,x2 = map(int, input().split(','))
x3,x4 = map(int, input().split(','))
print(check_overlap(x1,x2,x3,x4))