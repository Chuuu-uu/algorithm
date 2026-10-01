T = int(input())

for tc in range(1, T + 1) :
    N = int(input())
    c = list(map(int, input().split()))
    answer = 1
    best = 1

    for i in range(N - 1) :
        if c[i] < c[i+1] :
            best += 1
        else :
            best = 1

        if best > answer :
            answer = best

    print(f'#{tc} {answer}')