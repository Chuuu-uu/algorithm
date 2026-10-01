# level: 3?
# (r, c) == (N-1, N-1): 종료조건
di = [0, 1]
dj = [1, 0]

def is_valid(i, j) :
    return 0 <= i < N and 0 <= j < N

# i, j: 현재 내 위치 행 번호, 열 번호 (재귀단계를 나타냄)
# now_sum: 현재까지 내가 거쳐온 칸들에 적혀있던 숫자의 합
def solve(i, j, now_sum) :
    global answer

    # 기저조건: 맨 오른쪽 아래에 도착 시 종료
    if (i, j) == (N-1, N-1) :
        # 내가 현재까지 거친 숫자들의 합이 최소인가
        # now_sum이 최소인지 확인
        if now_sum < answer :
            answer = now_sum
        return

    # 재귀호출
    # 다음단계로 갈 때 선택 가능한 경우의 수 2가지(오른쪽 or 아래 이동)
    # d: 0 오른쪽 / d: 1 아래
    for d in range(2) :
        ni = i + di[d]
        nj = j + dj[d]
        if is_valid(ni, nj) :
            # 다음단계로
            # 다음단계로 갈 때 선택 가능한 경우의 수 2가지 (오른쪽, 아래)
            solve(ni, nj, now_sum + matrix[ni][nj])

T = int(input())

for tc in range(1, T + 1) :
    N = int(input())

    # 2차원 배열
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 답: 최소합
    answer = 10000

    # 맨 왼쪽 위에서 출발, 시작지점 숫자 합에 더하고 시작
    solve(0, 0, matrix[0][0])

    print(f'#{tc} {answer}')