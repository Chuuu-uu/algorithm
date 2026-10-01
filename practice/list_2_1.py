# 5 x 5 2차원 배열에 25개의 숫자를 저장하고, 대각선 원소의 합을 구하시오

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N) :
    ans += arr[i][i] + arr[i][N-1-i]

if N % 2 : # N이 홀수인 경우에만 중심 원소가 겹침
    ans -= arr[N//2][N//2]  # 가운데 겹치는 거 빼기 (홀수일 때만)
print(ans)