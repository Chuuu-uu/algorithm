# 5 x 5 2차 배열에 25개의 숫자를 저장하고, 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오
# 25개의 요소에 대해 모두 조사하여 총 합을 구하시오
# 벽에 있는 요소는 이웃한 요소가 없을 수 있음에 주의하시오

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total = 0
for i in range(N) :
    for j in range(N) :
        s = 0  # i, j 이웃과 차이의 절대값의 합
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]] :
            ni, nj = i + di, j + dj   # 이웃 원소의 인덱스 후보
            if 0 <= ni < N and 0 <= nj < N :   # 존재하는 인덱스면
                s += abs(arr[i][j] - arr[ni][nj])
        total += s
print(total)