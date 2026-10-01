# 마지막 노드 번호 V, 간선의 개수 N (V-1)
V, N = map(int, input().split())
# 트리의 정보가 한줄로 입력
tree = list(map(int, input().split()))
# 간선의 개수만큼 잘라서 2개 쌍
# 5 4
# 1 2 1 3 3 4 3 5
# 앞: 부모번호 뒤: 자식번호
# 1 2 / 1 3 / 3 4 / 3 5

# 자식 노드 번호를 인덱스로 사용하는 방법
parent = [0] * (V + 1)
# parent[2] = 2번 노드의 부모 노드 번호
# parent[4] = 4번 노드의 부모 노드 번호
# x번 노드의 부모 노드 번호를 알고싶음 -> parent[x]

for i in range(N) :
    p = tree[i*2]
    c = tree[i*2+1]

    # 자식 노드 번호를 인덱스
    parent[c] = p

print(parent)

# 5번 노드의 조상 노드 목록 구하고 싶음
child = 5
a = []  # 조상 목록
# child의 부모 노드가 있다면 -> child는 루트 노드가 아님
# 루트 노드가 아닐 경우 위로 한 단계 올라가서 반복
while parent[child] != 0 :
    child = parent[child]
    # 이 노드는 원래 노드의 부모 노드니까 조상 목록에 추가
    a.append(child)

print(child, a)  # 루트 노드, 조상 목록