def maxAreaBF(height):
    '''
    BruteForce
    :param height:
    :return: maxheight -> res
    '''
    res = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = abs(i-j) * min(height[j], height[i])
            res = max(res, area)
    return res

height = [1,8,6,2,5,4,8,3,7]
# Expected output: 49
print(f"Area with Brute Force = {maxAreaBF(height)}")
'''
time : O(n**2)
space: O(n)
'''

def maxArea(height):
    l = 0
    r = len(height)-1
    area = 0
    while l < r:
        print(f"In height {height[l]} & {height[r]}, r= {r}")
        area = max(area, min(height[l], height[r]) * (r - l))
        print(f"Area = {area}")
        if height[l] <= height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
    return area

print(f"Area with 2 pointer optimisation = {maxArea(height)}")

'''
Time & Space : O(n)
'''