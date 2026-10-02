T = int(input())

for tc in range(1, T + 1) :
    N, M = map(int, input().split())

    panel = [list(map(int, input().split())) for _ in range(N)]
    lens = [list(map(int, input().split())) for _ in range(M)]

    print(f'#{tc}')
    for i in range(N-M+1) :
        for j in range(N-M+1) :
            energy = 0

            for r in range(M) :
                for c in range(M) :
                    energy += panel[i+r][j+c] + lens[r][c]

            print(energy, end = ' ')
        print()
