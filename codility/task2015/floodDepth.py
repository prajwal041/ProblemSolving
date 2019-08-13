def solution(a):
    import sys
    maxleft = 0
    bottom = sys.maxsize
    result = 0
    for i in a:
        if i > maxleft:
            depth = (maxleft-bottom) if (maxleft-bottom)>0 else 0
            result = max(result, depth)
            maxleft=i
            bottom=sys.maxsize
            continue
        bottom = min(bottom,i)
        depth = i - bottom
        result = max(result, depth)
    return result

a = [1,3,2,1,2,1,5,3,3,4,2]
print(solution(a))