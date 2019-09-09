def dfs(u):
    for v in adj[u]:
        if dist[v] == INF:
            dist[v] = dist[u] + 1
            print("Distance")
            print(dist[v], v)
            dfs(v)


n = int(input())
adj = [[] for i in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

INF = int(1e9)
dist = [INF] * (n + 1)
girls = [0] * (n + 1)
m = int(input())
for i in range(m):
    x = int(input())
    girls[x] = 1
dist[1] = 0
dfs(1)
indexRes = 0
for i in range(1, n + 1):
    if girls[i] == 1:
        if dist[indexRes] > dist[i]:
            print(dist[indexRes], dist[i])
            indexRes = i
print(indexRes)

