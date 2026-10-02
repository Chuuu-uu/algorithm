T = int(input())


# i : 재료 번호, 단계
# score: 현재 재료까지 선택했을 때 맛 점수
# cal: 현재 재료까지 선택했을 때 칼로리
def diet(i, score, cal):
    global max_score

    # 0. 가지치기
    if cal > K :
        # 문제에서 제시한 제한 칼로리보다 크면 안됨

        return

    # 남은 재료의 점수를 다 합해도 내가 이전에 구한 최고 점수보다 낮으면 진행할 필요가 없다
    remain = 0
    for j in range(i, N) :
        remain += matrix[j][0]
    if score + remain < max_score :
        return

    # 1. 기저 조건(종료 조건)
    if i == N:
        max_score = max(max_score, score)
        return

    # 2. 재귀 호출(다음 단계)
    # 햄버거에 i번 재료를 포함하는 경우
    diet(i + 1, score + matrix[i][0], cal + matrix[i][1])
    # 햄버거에 i번 재료를 포함하지 않는 경우
    diet(i + 1, score + 0, cal + 0)


for tc in range(1, T + 1):
    # 재료 개수 N, 제한 칼로리 K
    N, K = map(int, input().split())

    # N개의 재료에 대한 맛 점수와 칼로리
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 답 : 제한 칼로리 이하에서 최고의 맛 점수
    max_score = 0

    # 다이어트 시작, 0번재료부터, 점수 0점부터, 칼로리 0부터
    diet(0, 0, 0)

    print(f'#{tc} {max_score}')