T = int(input())

for tc in range(1, T + 1) :
    N = int(input())

    farm = []

    for _ in range(N) :
        row = list(map(int, input()))
        farm.append(row)

    mid = N // 2

    total = 0

    for i in range(N) :
        d = abs(mid - i)

        start = d
        end = N - d

        for j in range(start, end) :
            total += farm[i][j]

    print(f'#{tc} {total}')


