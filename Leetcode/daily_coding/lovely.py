# num = 100
# maps = {}
# while num!=0:
#     nums = num%10
#     num = num//10
#     if nums not in maps:
#         maps[nums]=1
#     else:
#         maps[nums]+=1
#
# # for i in range(str(len(num))):
# #     maps[num[i]]=1
#
# print(maps)
# for i in maps.values():
#     if i>3:
#         print(False)
#     else:
#         print(True)




def solution(A, B):
    if A==0 and B==0:
        return 1
    for i in range(A,B+1):
        # print(i)
        n = str(i)
        if len(n) - len(set(n)) >= 2:
            return i - 1


        # num = int(i)
        # maps = {}
        # while num!=0:
        #     nums = num %10
        #     num = num // 10
        #     if nums not in maps:
        #         maps[nums] = 1
        #     else:
        #         maps[nums]+=1
        # for j in maps.values():
        #     print(maps.get(j))
        #     if j>3:
        #         print(maps[j])

print(solution(1,111))
# def solution(s, k):
#     s1 = ""
#     num = len(s)
#     if num<k:
#         return s
#     for i in range(len(s)-1):
#         if i<k:
#             s1+=s[i]
#     # print(s1)
#     s2 =""
#     for i in range(len(s1)-1,-1,-1):
#         if s1[i]!=" ":
#             s1 = s1[:-1]
#         else:
#             break
#     return s1


