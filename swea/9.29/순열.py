# # level 3 branch 6
# path = []
#
# def kfc(x) :
#     if x == 3 :
#         print(path)
#         return
#     for i in range(1, 7) :
#         path.append(i)
#         kfc(x + 1)
#         path.pop()
# kfc(0)

# 순열
path = []
used = [0] * 3
def kfc(i) :
    if i == 3 :
        print(path)
        return

    for j in range(3) :
        if used[j] :
            continue
        used[j] = 1
        path.append(j)
        kfc(i+1)
        used[j] = 0
        path.pop()
kfc(0)

# 순열2
path = []
used = [0] * 3
numbers = [5, 6, 7]

def kfc(i) :
    if i == 3 :
        print(path)
        return

    for j in range(3) :
        # j번 인덱스 숫자를 이전에 사용했다면
        if used[j] :
            # 다른 숫자로
            continue

        # j번 인덱스 숫자를 사용한다고 체크
        used[j] = 1
        path.append(numbers[j])
        kfc(i+1)
        used[j] = 0
        path.pop()
kfc(0)