que = [0] * 10
front = rear = -1

rear += 1    # enqueue(1)
que[rear] = 1
rear += 1    # enqueue(2)
que[rear] = 2
rear += 1    # enqueue(3)
que[rear] = 3

####
front += 1
print(que[front])
front += 1
print(que[front])
front += 1
print(que[front])

####
while front != rear :
    front += 1
    print(que[front])

####
q = []  # 큐 생성
q.append(1)
q.append(2)
q.append(3)
print(que[front])
print(que[front])
print(que[front])
