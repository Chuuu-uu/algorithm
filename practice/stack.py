# # 파이썬의 리스트 메서드를 사용한 방법
#
# # 스택 초기화
# # 스택으로 사용할 리스트 선언
# stack = []
#
# # 스택에 자료 추가
# for i in range(1, 11) :
#     stack.append(i)
#
# print(stack)
#
# # stack이라는 변수는 '스택'이라는 자료구조로 사용할 것이기 때문에
# # 아래 코드는 사용하지 않음
# # stack[2] = 16
#
# # 스택에서 자료를 삭제 (pop)
# for i in range(10) :
#     e = stack.pop()
#     print(e, end='')
# print()
#
# print(stack)
#
# while stack :
#     e = stack.pop()
#     print(e, end='')
# print()
# print(stack)
#######################################################
# # top을 사용한 스택
# # 스택의 크기
# N = 10
# # top: 스택에서 꼭대기에 저장된 자료의 위치 (빈 상태에서는 -1)
# # 마지막에 삽입된 자료의 위치 (인덱스)
# top = -1
#
# # 스택 초기화
# stack = [0] * N
#
# # 스택에 자료 추가하기 (push)
# for i in range(1, 11) :
#     if top == N-1 :
#         print('overflow')
#         break
#     else :
#         top += 1
#         stack[top] = i
# print(stack, top)
#
# # 스택에서 자료를 삭제하기 (pop)
# for i in range(10):
#     if top > -1 :
#         e = stack[top]
#         top -= 1
#         print(e, end='')
#     else :
#         print('underflow')
#         break
# print()
#############################################
# # 피보나치 수열의 n번 항 구하기
# def fibo(n) :
#     if n < 2 :
#         # 0번항, 1번항 => 0, 1
#         return n
#     else :
#         # 나머지: n-1번항 + n-2번항
#         return fibo(n-1) + fibo(n-2)
# print(fibo(7))
##################################################
# 2차원 리스트를 재귀함수로 순회하기
N = 5

matrix = [[N * i + j for j in range(1, N +1)] for i in range(N)]

# 2차원 리스트 반복문 순회 (행 우선 순회)
# i = 0, j = 0 => i = 0, j = 1 ... i = 0, j = 4
# i = 1, j = 0 => i = 1, j = 1 ... i = 1, j = 4
# ...
# i = 4, j = 0 => i = 4, j = 1 ... i = 4, j = 4
for i in range(N) :
    for j in range(N) :
        print(matrix[i][j], end = ' ')
    print()

# 재귀함수
# 반복문의 각 단계를 나타내는 파라미터 i, j 필요
def myprint(i, j) :
    # 1. 종료조건 => i, j를 통해서 어떻게 나타낼 수 있는지, return
    if i == N:
        return
    # 2. 재귀호출 => 현재 단계에서 필요한 작업을 수행한 후에 다음 단계 재귀호출
    print(matrix[i][j], end = ' ')

    if j == N -1 :
        print()
        myprint(i + 1, 0)
    else :
        myprint(i, j + 1)


myprint(0, 0)


# 강사님 코드
def myprint(i, j) :
    if i >>= N :
        return
    print(matrix[i][j], end = ' ')
    j += 1
    if j == N :
        j = 0
        i += 1
        print()
    myprint(i, j)
print('===================')