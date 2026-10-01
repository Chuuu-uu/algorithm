# 재귀 이용해서 출력해보기
# 0 1 2 3 2 1 0
def abc(level) :
    print(level, end = ' ')
    if level == 3 :
        return

    abc(level + 1)
    print(level, end = ' ')
abc(0)


# 0 1 2 3 4 5 5 4 3 2 1 0
def abc(level) :
    if level == 5 :
        print(level, end=' ')
        return
    print(level, end = ' ')
    abc(level + 1)
abc(0)

# 누적합 구하기 - 재귀 DFS 구현시 변수를 global 선언하는가? 에 따른 차이
# 전역변수
arr = [1, 3, 5, 7]
Sum = arr[0]

def abc(level) :
    global Sum

    if level == 3 :
        print(Sum, end = ' ')
        return
    Sum += arr[level + 1]
    abc(level + 1)
    Sum -= arr[level + 1] # 전역변수로 했을 때 원상복구 하기 위해 빼야됨
    print(Sum, end = ' ')

abc(0)

# 지역변수
def abc(level, Sum) :
    if level == 3 :
        print(Sum, end = ' ')
        return

    abc(level, Sum + arr[level + 1])
    print(Sum, end = ' ')

abc(0, arr[0])

# level = 3
# branch = 4
card = 'ABCD'
path = ['']*3

def abc(level) :
    if level == 3 :
        for i in range(level) :
            print(path[i], end = ' ')
        print()
        return
    for i in range(4) :
        path[level] = card[i]
        abc(level + 1)
abc(0)

# 완전탐색
arr = [3, 4, 7, 1, 6]
cnt = 0

def abc(level, Sum) :
    global cnt
    if Sum > 10 # 가지치기
        return

    if level == 3 :
        if Sum == 10 :
            cnt += 1
        return

    for i in range(5) :
        abc(level + 1, Sum + arr[i])  # level 1씩 증가 / Sum 내가 앞으로 들어갈 가지 더하기

abc(0, 0)  # level, Sum
print(cnt)

# 전역변수
# 완전탐색
arr = [3, 4, 7, 1, 6]
cnt = 0
Sum = 0

def abc(level):
    global cnt, Sum

    if Sum > 10  # 가지치기
        return

    if level == 3:
        if Sum == 10:
            cnt += 1
        return

    for i in range(5):
        Sum += arr[i]
        abc(level + 1)  # level 1씩 증가 / Sum 내가 앞으로 들어갈 가지 더하기
        Sum -= arr[i]

abc(0)  # level
print(cnt)