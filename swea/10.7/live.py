# 우선순위 큐
import heapq
arr = []
heapq.heappush(arr, 13)  # min heap이 디폴트값
heapq.heappush(arr, 5)
heapq.heappush(arr, 17)
heapq.heappush(arr, 9)
print(arr)
# 1
for i in range(len(arr)) :
    print(heapq.heappop(arr), end = ' ')
# 2
while arr :
    node = heapq.heappop(arr)
    print(node, end = ' ')
# max heap
arr = [3, 234, 23, 12, 31]
heap = []
for i in range(len(arr)) :
    heapq.heappush(heap, -arr[i])
for i in range(len(arr)) :
    print(heapq.heappop(heap)*-1, end = ' ')
    print(-heapq.heappop(heap), end=' ')
# heapify 사용
arr = [3, 234, 23, 12, 31]
arr = list(map(lambda x: -x, arr))  # arr 배열의 모든 원소에 - 붙인 후, arr에 재할당
heapq.heapify(arr)
for i in range(len(arr)) :
    print(-heapq.heappop(arr), end = ' ')
###############################
