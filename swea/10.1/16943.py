T = int(input())


for tc in range(1, T + 1) :
    N, M = map(int, input().split())
    A = list(map(int, input().split())) # 정렬 대상
    B = list(map(int, input().split())) # 검색 대상

    # 문제에서 원하는 답
    # B에서, A 안에 있으면서 이진검색을 할 때 왼쪽 오른쪽 번갈아가며 찾아낸 원소의 개수
    # 제약조건을 종합해보면, 같은 방향을 연속으로 선택하지만 않으면 된다
    cnt = 0

    # 이진검색을 위해 정렬
    A.sort()

    # B에 있는 숫자 하나씩 꺼내서 A에서 찾아보기
    for i in B :
        # B 안에 있는 숫자 i를 A에서 이진검색을 통해 찾아보자
        # 한 방향을 연속으로 선택하게 되면 fail

        # 이진검색 범위 (시작, 종료)
        left = 0
        right = N - 1

        # 내가 이전에 선택한 방향, 처음은 -1로, 왼쪽은 0, 오른쪽은 1로
        D = -1

        while left <= right :
            mid = (left + right) // 2
            if A[mid] ==  i :
                # 찾음
                cnt += 1
                break

            elif A[mid] > i :
                # 내가 찾는 값 i가 가운데 값보다 작았으니까
                # 왼쪽 방향 선택
                right = mid - 1
                # 내가 만약 이전에도 왼쪽을 선택했었다면? 조건위반
                if D == 0 :
                    break
                else :
                    D = 0

            else :
                # 내가 찾는 값 i가 가운데 값보다 컸으니까
                # 오른쪽 방향 선택
                left = mid + 1
                # 내가 만약 이전에도 오른쪽을 선택했었다면? 조건 위반
                if D == 1 :
                    break
                else :
                    D = 1



    print(f'#{tc} {cnt}')