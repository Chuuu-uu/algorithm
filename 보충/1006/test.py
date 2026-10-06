T = int(input())

for tc in range(1, T + 1) :
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in range(N-M+1) :
        for j in range(N-M+1) :
            fly = []
            for r in range(M) :
                for c in range(M):
                    cost += board[i+r][j+c] - board[i][j]

            if cost > answer :
                answer = cost

    print(f'#{tc} {answer}')
