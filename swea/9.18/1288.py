T = int(input())

for tc in range(1, T + 1) :
    N = int(input())

    v = [0] * 10

    k = 0

    while True :
        k += 1
        num = N * k

        for d in str(num) :
            v[int(d)] = 1

        if sum(v) == 10 :
            break
    print(f'#{tc} {num}')
