# 6자리 숫자 입력
numbers = list(map(int, input()))
answer = False

# level: 6, branch: 6
# i: 단계를 나타낼 파라미터
# path: 각 단계에서 고른 숫자 저장
# used: 각 단계에서 사용한 인덱스 체크
# 지금까지 만든 순열의 상태를 나타냄
def perm(i, path, used) :
    global answer
    # 기저조건
    if i == 6 :
        # 순열을 완성한 상태
        # path에서 앞3/뒤3 앞 뒤가 각각 run or triplet 이면 baby-gin
        run1 = (path[0] + 1 == path[1] and path[1] + 1 == path[2])
        run2 = (path[3] + 1 == path[4] and path[4] + 1 == path[5])
        trip1 = (path[0] == path[1] == path[2])
        trip2 = (path[3] == path[4] == path[5])

        if (run1 or trip1) and (run2 or trip2) :
            answer = True
        return

    # 재귀호출
    # j: i단계에서 고를 숫자의 인덱스
    for j in range(6) :
        # 이전에 j번 인덱스에 있는 숫자를 사용했는지 확인
        # 사용했다면 다른 인덱스에 있는 숫자를 사용하도록 건너뜀
        if used[j] :
            continue

        # j번 숫자 사용 체크
        used[j] = 1
        # j번 숫자 순열에 넣고
        path.append(numbers[j])
        perm(i + 1, path, used)
        # j번 숫자 순열에서 제거
        # j번 숫자 사용 해제
        used[j] = 0
        path.pop()

# 0단계부터 시작, 순열 초기 상태(아무것도 선택 안 함), 사용한 인덱스(아무것도 사용 안 함)
perm(0, [], [0]*6)

if answer :
    print('Yes')
else :
    print('No')