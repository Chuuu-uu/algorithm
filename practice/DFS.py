# 인접 행렬
# A = 0, B = 1, .. G = 6
# 정점의 개수 N = 7개

# adj_matrix = []
# 1번 정점과 2번 정점이 인접해있다.
# adj_matrix[1][2] = 1
# adj_matrix[2][1] = 1 (단, 방향이 있는 그래프라면 0일 수도 있다)
# 3번 정점과 4번 정점이 인접해있지 않다.
# adj_matrix[3][4] = 0
# adj_matrix[4][3] = 0

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, input().split())
# 그래프의 연결 정보가 한 줄로 입력
G = list(map(int, input().split()))

adj_matrix = [[0] * (V + 1) for _ in range(V+1)]

for i in range(E) :
    s = G[2 * i]
    e = G[2 * i + 1]
    adj_matrix[s][e] = 1
    adj_matrix[e][s] = 1

print(*adj_matrix, sep = '\n')

############################
adj_list = [[] for _ in range(V + 1)]

# adj_matrix[4] = [1, 2, 3]: 4번 정점과 1, 2, 3번 정점이 인접해있다
# adj_matrix[2] = []: 2번 정점과 연결된 정점이 없다

for i in range(E) :
    s = G[2 * i]
    e = G[2 * i + 1]
    adj_matrix[s][e] = 1
    adj_matrix[e][s] = 1

print(*adj_list)
###################################
# s: 탐색 시작 정점 번호
# V: 정점의 개수
def dfs(s, V) :
    # DFS: 깊이 우선 탐색, 그래프의 모든 정점을 빠짐없이 한번씩 모두 탐색
    visited = [0] * (V + 1)
    # visited[5] = 1: 5번 정정은 이전에 방문한적이 있다
    # visited[4] = 0: 4번 정점은 이전에 방문한적이 없다

    # 돌아올 곳을 기억할 스택
    stack = []

    visited[s] = 1
    # 현재 내가 위치한 정점 번호 v
    v = s
    print(v)

    while True :
        # 현재 내가 있는 정점 번호: v
        # v와 인접한 정점 중에 간적이 없는 정점 w를 찾는다
        # 돌아올 정점번호 v를 스택에 저장하고, w를 새로운 v로 지정해서 탐색을 반복
        for w in range(V + 1) :
            # v와 w가 인접해있고, w를 방문한적이 없다면
            if adj_matrix[v][w] and not visited[w] :
                # v를 스택에 저장하고  w로 바로 이동
                stack.append(v)
                visited[w] = 1
                print(w)
                v = w
                # 새로 바뀐 v에서 연결된 정점을 찾아야 하므로 break
                break
        else :
            # 반복문에서 break 되지 않았다면 => 이동 할 수 있는 w를 찾지 못함, 갈 길이 없다
            # 이전 정점으로 되돌아가서 새로운 길을 찾아야 한다
            # => stack.pop() 하면 가장 최근에 방문한 정점 번호를 알아낼 수 있다.
            if stack :
                v = stack.pop()
            else :
                # while break
                # 스택에 더이상 돌아갈 정점이 없다면 모든 정점을 다 방문했다
                break