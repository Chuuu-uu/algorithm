T = int(input())

for tc in range(1, T + 1) :
    # 자연수 개수 입력
    N = int(input())
    # 자연수
    Ai = list(map(int, input().split()))
    # 문제에서 원하는 답: 차례대로 감소
    answer = 1

    for i in range(N-1) :
        # i +1번째 자연수가 i보다 크거나 같으면 제대로 감소하지 않음
        if Ai[i] <= Ai[i + 1] :
            answer = 0


    print(f'#{tc} {answer}')