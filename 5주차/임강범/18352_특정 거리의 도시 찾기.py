import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)
# N : 도시 갯수, M : 간선 갯수, K : 최단거리, X : 출발노드 
N, M, K, X = map(int,input().split())

# 입력받은 간선의 정보를 graph에 작성
graph = [[] for _ in range(N+1)] 
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append((b, 1))

# 출발지점부터 최단거리를 담을 distance 리스트 생성후 무한대로 초기화
distance = [INF]  * (N+1)

# 우선순위 큐 생성
q = []
heapq.heappush(q,(0,X)) # 출발지점을 거리를 0으로 우선순위 큐에 삽입
distance[X] = 0 
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: # 방문처리한 도시 스킵
        continue
    for i in graph[now]: # 인접노드 갱신, i[0]:도시이름, i[1]:거리
        cost = dist + i[1] # cost는 현재 노드까지의 거리 + 현재 노드와 인접 노드 사이의 거리
        if distance[i[0]] > cost: # cost 값 즉 거쳐가는 값이 작다면 초기화 후 우선순위 큐에 삽입
            distance[i[0]] = cost
            heapq.heappush(q,(cost, i[0]))

flag = 0
for i in range(N+1):
    if distance[i] == K:
        flag = 1
        print(i)
if flag == 0:
    print(-1)