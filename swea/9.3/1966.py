# 선택정렬
T = int(input())
for tc in range(1, T + 1) :
    # N개의 숫자 정렬
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N-1) :
        # i번 인덱스 자리 주인 찾기
        # 0번 -> 최소값
        # 1번 -> 그 다음 최소값
        # 2번 -> 그 다음 다음 최소값

        # 최소값의 위치 (일단 i에 있다고 가정)
        min_idx = i
        # i뒤에서부터 최소값 찾기 시작
        for j in range(i+1, N) :
            if numbers[min_idx] > numbers[j] :
                min_idx = j

        # 최소값이 있는 위치, i 위치에 있는 원소를 교환
        numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]

    print(f'#{tc}', *numbers)


# 버블정렬
T = int(input())
for tc in range(1, T + 1) :
    # N개의 숫자 정렬
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N - 1):
        # 뒤에서부터 큰 숫자를 하나씩 확정
        for j in range(N - 1 - i):
            # 앞의 숫자가 더 크면 교환
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(f'#{tc}', *numbers)


# 카운팅 정렬
T = int(input())

for tc in range(1, T + 1):
    # N개의 숫자 정렬
    N = int(input())
    numbers = list(map(int, input().split()))

    count = [0] * (30)

    # 숫자 확인하면서 개수 1개씩 증가
    for num in numbers :
        count[num] += 1

    # 정렬된 결과를 저장할 리스트
    answer = []

    # 0~29 까지 작은 숫자부터 확인
    for num in range(30) :
        # 해당 숫자가 나온 횟수
        cnt = count[num]

        # 나온 횟수만큼 result에 추가
        for _ in range(cnt) :
            answer.append(num)

    print(f'#{tc}', *answer)

