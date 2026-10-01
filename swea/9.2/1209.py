# 10개의 테스트 케이스 주어짐
for _ in range(10) :
    # 테스트 케이스 번호
    tc = int(input())

    # 100 x 100
    arr = [list(map(int, input().split())) for _ in range(100)]

    answer = 0

    # 행의 합
    for i in range(100) :
        row_sum = 0
        for j in range(100) :
            row_sum += arr[i][j]
        # 현재 행의 합과 기존 최댓값 비교
        # 한 행의 합을 구할 때마다 최댓값 확인
        answer = max(answer, row_sum)

    # 열의 합
    for j in range(100) :
        col_sum = 0
        for i in range(100) :
            col_sum += arr[i][j]
        answer = max(answer, col_sum)

    # 왼 -> 오 대각선
    diag1 = 0

    for i in range(100) :
        diag1 += arr[i][i]
    answer = max(answer, diag1)

    # 오 -> 왼 대각선
    diag2 = 0
    for i in range(100) :
        diag2 += arr[i][99-i]
    answer = max(answer, diag2)

    # 답 출력
    print(f'#{tc} {answer}')

