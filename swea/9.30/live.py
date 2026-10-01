# name = 'ABC'
#
# def abc(level, path) :
#     if level == 3 :
#         print(*path)
#         return
#
#     abc(level + 1, path)
#     abc(level + 1, path + [name[level]])
#
# abc(0, [])

# p.17
arr = = ['A', 'B', 'C']
n = len(arr)

for tar in range(1<<n) :
    answer = []
    for i in range(n) :
        if tar & 1 :   # if tar & 0x1
            answer.append(arr[i])
        tar >>= 1

    print(answer)

#  순열
caard = 'ABCD'
path = [""]*3
used = [0]*4

def abc(level) :
    if level == 3 :
        print(*path)
        return

    for i in range(4) :
        if used[i] == 1 : continue
            path[level] = card[i]
            abc(level + 1)
            path[level] = ''
            used[i] = 0

# p.30
