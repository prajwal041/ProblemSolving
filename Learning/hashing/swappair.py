for _ in range(int(input())):
    m,n = input().split()
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    val = abs(sum(arr1)-sum(arr2))
    seen_dict = {}
    for i in range(len(arr1)):
        if val - arr1[i] in arr2:
            print(arr1[i],arr2[i])
            print("1")
            break
        else:
            pass