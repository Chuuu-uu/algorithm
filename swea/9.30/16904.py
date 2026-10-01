T = int(input())

for tc in range(1, T + 1) :
    # 화물차 N개
    N = int(input())

    # 화물차i번 [시작시간, 종료시간]
    # 화물차0번 [S0, E0], 화물차1번 [S1, E1]
    work_list = [list(map(int, input().split())) for i in range(N)]
    # [[S0, E0], [S1, E1], [S2, E2], ... [SN-1, EN-1]]
    # 정렬기준: 종료시간
    # work_list의 원소 하나를 e라고 했을 때 e[1]이 종료 시간
    work_list.sort(key = lambda e: e[1])
    # def key_f(e):
    #       return e[1]
    # work_list.sort(key=key_f)

    # 문제에서 원하는 답: 최대 작업 개수
    answer = 0

    # 이 전에 끝난 작업의 종료 시간
    last = 0
    for i in range(N) :
        # 작업시간 빠른 순서대로 튀어나온다
        # 이전에 끝난 작업의 종료 시간 이후에 시작하는 작업만 골라서 선택
    print(f'#{tc} {answer}')

