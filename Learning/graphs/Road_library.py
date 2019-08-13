# from collections import deque
# def generate_graph(connections):
#     graph = {}
#     for con in connections:
#         graph[con[0]] = [con[1]] if con[0] not in graph else graph[con[0] + con[1],]
#         graph[con[1]] = [con[0]] if con[1] not in graph else graph[con[0] + con[1],]
#     return graph
#
# def roadlib(n,cities, clib, croad):
#     graph = generate_graph(cities)
#     visited = set()
#     q = deque()
#     road_count = 0
#     lib_count = 0
#     if clib < croad:
#         return n*clib
#     for city in range(1, n+1):
#         if city not in visited:
#             lib_count+=1
#             q.append(city)
#             visited.add(city)
#             while q:
#                 n = q.pop()
#                 if n in graph:
#                     for nbour in graph[n]:
#                         if nbour not in visited:
#                             road_count+=1
#                             q.append(nbour)
#                             visited.add(nbour)
#     return road_count*croad+ lib_count*clib
#
# print(roadlib(3,[1,3],2,1))




def dfs(s):
    global visited,alist,valCount,croad,cost
    visited[s]=1;l=len(alist[s]);valCount+=1
    if(l!=0):
        for i in range(l):
            if(visited[alist[s][i]]==0):
                dfs(alist[s][i])
                cost+=croad
q = int(input().rstrip())
valCount=0
for a0 in range(q):
    cost=0
    n,m,clib,croad=map(int,input().split())
    visited=[0 for i in range(n+1)];alist=[[] for i in range(n+1)]
    count=0;roads=0;road=[];current=0
    for a1 in range(m):
        city_1, city_2 = map(int,input().split(' '))
        alist[city_1].append(city_2);alist[city_2].append(city_1)
    if(m==0 or croad>=clib): print(n*clib)
    else:
        for i in range(1,n+1):
            if(visited[i]==0):
                valCount=0
                dfs(i)
                cost+=clib
        print(cost)

'''
Input:
2
3 3 2 1
1 2
3 1
2 3
6 6 2 5
1 3
3 4
2 4
1 2
2 3
5 6

Output:
4 
12

T ~ O(n2)

'''