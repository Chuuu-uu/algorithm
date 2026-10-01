def f(i, N) :
    if i == N :  # 중단 조건
        return
    else :
        f(i + 1, N)  # 재귀호출

f(0, 5)