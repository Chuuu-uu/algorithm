# 현재 방 번호: now
# 내가 지금까지 들른 방 번호 모음: visited
# 내가 지금까지 사용한 에너지 사용량: e
def solve(now, visited, e) :
    global answer

    # 종료조건
    if len(visited) == N :
        e += Energy[now][0]
        # e가 최소인지 확인
        if e < answer :
            answer = e
        return

    # 재귀호출
    # 내가 지금까지 들린적 없는 구역 선택해서 이동
    for i in range(N) :
        # 내가 i번 구역을 간적이 없다면
        if i not in visited :
            # i번 구역으로 이동, i번 방문 목록에 추가, now -> i 에너지 사용량 더하기
            solve(i, visited + [i], e + Energy[now][i])


T = int(input())

for tc in range(1, T + 1) :
    # 구역의 개수
    N = int(input())

    # 이동하면서 사용하는 배터리 양
    # Energy[i][j] => i번 구역에서 j번 구역으로 가는데 소비하는 에너지 양
    # Energy[i][j] != Energy[j][i]
    Energy = [list(map(int, input().split())) for _ in range(N)]
    answer = float('inf')

    # 0번 사무실에서 출발
    solve(0, [0], 0)

    print(f'#{tc} {answer}')
