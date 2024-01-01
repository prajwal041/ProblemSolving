def largestRectangle(heights):
    '''
    :param heights:
    :return: maxArea - > area
    '''
    area = 0
    stack = [] # pair: (index, height)
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            area = max(area, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        area = max(area, h * (len(heights) - i))
    return area

heights = [2,1,5,6,2,3]
print(largestRectangle(heights))

'''
Time & Space: O(n)
'''