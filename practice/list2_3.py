# 10개의 정수를 입력받아 부분집합의 합이 0이 되는 것이 존재하는지 확인
arr = [-7, -5, 2, 3, 8, -2, 4, 6, 9, 12]
N = len(arr)
ans = 'N'
# 각 자리를 이진수로 표현 (10자리라 0~1023)
for i in range(1, 1 << N) :  # 2 ** N: 부분집합을 표현할 비트 생성
    s = 0
    for j in range(N) :   # 검사할 비트 번호 j
        if (i & 1 << j) :    # j번 비트가 1이면 arr[j]가 부분집합의 원소
            s += arr[j]
    if s == 0 :
        ans = 'Y'
        break # for i
print(ans)
