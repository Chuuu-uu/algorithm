# 정렬 대상 리스트
arr = [69, 10, 30, 2, 16, 8, 31, 22]

# 분할 정복
# 분할하고 분할한 작은 부분을 정렬
# 합칠 때 정렬이 이루어짐

# m: 우리가 정렬하고 싶은 배열 (리스트)
def merge_sort(m) :
    # 종료 조건 (언제까지 분할할 것인지)
    if len(m) == 1 :
        return m
    # 분할
    # 반으로 쪼개서 왼쪽부분, 오른쪽 부분으로 분할
    mid = len(m) // 2
    # m[: mid]: left / m[mid:]: right
    left = m[:mid]
    right = m[mid:]


    # 정복
    left = merge_sort(left)
    right = merge_sort(right)

    # 합병
    return merge(left, right)

# 왼쪽 부분과 오른쪽 부분을 합치는 함수
# 합치면서 정렬이 진행됨
def merge(left, right) :
    # 최소값의 위치 (left와 right는 이미 정렬이 되어있는 상태)
    li = ri = 0

    result = []

    # 각 인덱스가 길이보다 작아야 유효안 인덱스
    # 왼쪽에 원소가 남아있거나 오른쪽에 원소가 남아있다면 반복
    while li < len(left) or ri < len(right) :
        # 1. 왼쪽과 오른쪽 둘 다 남아있는 경우
        if li < len(left) and ri < len(right) :
            # 왼쪽의 최소값과 오른족의 최소값 비교해서 더 작은 거 선택
            if left[li] <= right[ri] :
                # 왼쪽의 최소값이 더 작았으니까 왼쪽 선택
                result.append(left[li])
                # 그 다음 작은 값으로 이동동
                li += 1
            else :
                # 오른쪽의 최소값이 더 작은 경우
                result.append(right[ri])
                ri += 1

        # 2. 왼쪽만 남은 경우 -> 비교 대상 없으니가 쭉 이어 써줌
        elif li < len(left) :
            result.append(left[li])
            li += 1

        # 3. 오른쪽만 남은 경우
        elif ri < len(right) :
            result.append(right[ri])
            ri += 1

    # 위의 while문을 반복하면서 정렬이 된다
    return result

print(merge_sort(arr))

