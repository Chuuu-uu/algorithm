# 병합 정렬
arr = [2, 3, 5, 7, 1, 2, 5, 9]

def merge(start, end) :
    if start == end :
        return
    mid = (start + end) // 2

    merge(start, mid)
    merge(mid + 1, end)

    a = start
    b = mid + 1
    result = []

    while 1 :
        if a > mid and b > end : break
        if a > mid :
            result.append(arr[b])
            b += 1

        elif b > end :
            result.append(arr[a])
            a += 1
        elif arr[a] <= arr[b] :
            result.append(arr[a])
            a += 1
        else :
            result.append(arr[b])
            b += 1
    for i in range(len(result)) :
        arr[start + i] = result[i]
merge(0, 7)
print(*arr)

# 퀵 정렬
arr = [4, 7, 1, 6, 2, 8, 5, 3, 9]
start = 0
end = 8
pivot = start
a = start + 1
b = end

while 1 :
    while a < and arr[a] <= arr[pivot] : a += 1  # 배열범위 안이고, a의 값이 pivot보다 작다면
    while b >= start and arr[b]  > arr[pivot] : b -= 1 # 배열범위 안 + b의 값이 pivot보다 크다면
    if a > b : break
arr[b], arr[pivot]