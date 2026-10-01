T = int(input())

for tc in range(1, T + 1) :
    N = int(input())
    # 10 * 10 격자
    arr =[[0] * 10 for _ in range(10)]

    for _ in range(N) :
        r1, c1, r2, c2, color = list(map(int, input().split()))

        for r in range(r1, r2 + 1) :
            for c in range(c1, c2 + 1) :
                # 해당 칸에 색 더함
                arr[r][c] += color

    purple = 0

    # 보라색 구간
    for r in range(10) :
        for c in range(10) :
            if arr[r][c] == 3 :
                purple += 1
    print(f'#{tc} {purple}')



##########################################################
# 강사님 코드
T = int(input())

for tc in range(1, T + 1) :

    # 색칠 횟수
    N = int(input())

    # 종이
    paper = [[0] * 10 for _ in range(10)]

    purple = 0

    for _ in range(N) :
        # 색칠 정보 입력 받기 (색칠 시작 행 번호, 열 번호, 색칠 마지막 행 번호, 열 번호, 색)
        i1, j1, i2, j2, color = list(map(int, input().split()))

        # (i1, j1) ~ (i2, j2)까지 color로 색칠하기
        for i in range(i1, i2 + 1) :
            for j in range(j1, j2 + 1) :
                # 0: 흰색
                # 1: 빨간색
                # 2: 파란색
                # 3: 보라색 (1 + 2)
                paper[i][j] += color

                if paper[i][j] == 3 :
                    purple += 1

    print(f'#{tc} {purple}')