"""
Problem: Minimum Number of Operations to Move All Balls to Each Box
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

Solution: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/discuss/2107263/Python-O(n)-solution-with-explanation
Input: boxes = [1,1,0]
Output: output = [1,1,3]
"""

def minOperations(boxes: list):
    output = []
    pos_list = []

    for i in range(len(boxes)):
        if boxes[i] == 1:
            pos_list.append(i)

    if len(pos_list) == 0:
        return boxes

    rc, lc = len(pos_list), 0
    rs, ls = sum(pos_list), 0

    for i in range(len(boxes)):
        csum = rs - rc*i + lc*i - ls
        output.append(csum)

        if boxes[i] == 1:
            rs -= i
            ls += i
            rc -= 1
            lc += 1
    return output

boxes = [1,1,0]
print(minOperations(boxes))





