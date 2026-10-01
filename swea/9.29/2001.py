T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    # N-M+1: 시작 가능한 위치 개수
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly = 0

            for r in range(M):
                for c in range(M):
                    fly += board[i + r][j + c]

            if fly > answer:
                answer = fly
    print(f'#{tc} {answer}')
