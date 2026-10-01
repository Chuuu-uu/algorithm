# # 무한재귀
# def kfc(x) :
#     kfc(x+1)
#
# kfc(0)
# print('끝')
#
# # 기저조건
# def kfc(x) :
#     if x == 2 :
#         return
#     print(x)
#     kfc(x + 1)
#     print(x)
# kfc(0)
# print('끝')

# 0 1 2 3 4 5 5 4 3 2 1 0 을 재귀호출을 이용해 구현
# def kfc(x) :
#     if x == 6 :
#         return
#     print(x)
#     kfc(x + 1)
#     print(x)
# kfc(0)

# Depth 3, 재귀호출 개수 4개인 경우
def kfc(x) :
    if x == 3 :
        return
    for i in range(4) :
        kfc(x + 1)
        print(x)
kfc(0)