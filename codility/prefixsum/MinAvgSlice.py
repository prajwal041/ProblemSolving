def solution(a):
    min_avg_value = (a[0]+a[1])/2.0
    min_avg_pos = 0
    for i in range(len(a)-2):
        if (a[i]+a[i+1])/2.0<min_avg_value:
            min_avg_value = (a[i]+a[i+1])/2.0
            min_avg_pos =i
        if (a[i]+a[i+1]+a[i+2])/3.0<min_avg_value:
            min_avg_value = (a[i] + a[i + 1]+ a[i+2]) / 3.0
            min_avg_pos = i
    if (a[-1]+a[-2])/2.0 <min_avg_value:
        min_avg_value=(a[-1]+a[-2])/2.0
        min_avg_pos=len(a)-2
    return min_avg_pos

a =[4,2,2,5,1,5,8]
print(solution(a))