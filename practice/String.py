# # s1의 각 글자가 s2에 모두 존재하는가?
# s1 = input()
# s2 = input()
#
# ans = 'YES'  # 모두 있다고 가정하고, 하나라도 없으면 'NO'로 바꾸고 종료
# for ch in s1 :
#     if ch not in s2 :
#         ans = 'NO'
#         break  # for ch
# print(ans)
################################################################
# # 첫 줄에 N, 다음에 NxN 문자열. 'Z'가 존재하는가?
# N = int(input())
# txt = [input() for _ in range(N)]
#
# def find_Z(txt, N):
#     for i in range(N) :
#         for j in range(N) :
#             if txt[i][j] == 'Z' :
#                 return 'YES'
#     return 'NO'


# ans = 'NO'
# for row in txt :
#     if 'Z' in row :
#         ans = 'YES'
#         break # for row
# print(ans)
################################################################
# # 첫 줄에 N, 다음에 NxN 지도, 집중호우 피해구역, 피해구역 수는?
# N = int(input())
# txt = [input() for _ in range(N)]
#
# cnt = 0
# for i in range(N) :
#     for j in range(N) :
#        if txt[i][j] == '#' :
#            cnt += 1
# print(cnt)
################################################################
# # 첫 줄에 N, 다음에 NxN 문자열.
# # A B    패턴이 존재하는가?
# # C D
# def find_pat(text, N) :
#     pat = ['AB', 'CD']
#     for i in range(N-1) : # 기준위치 i, j
#         for j in range(N-1) :
#             cnt = 0
#             for r in range(2) :
#                 for c in range(2) :
#                     if text[i+r][j+c] == pat[r][c]:
#                         cnt += 1
#             if cnt == 4 :
#                 return 'YES'
#     return 'NO'
#
# N = int(input())
# text = [input() for _ in range(N)]
################################################################
# 첫 줄에 N, 다음에 NxN 미로, 0통로 1벽 # 로봇. 상하좌우로 모두 이동할 수 있는 칸 수는?
N = int(input())
text = [input() for _ in range(N)]

ans = 0  # 4 방향이 모두 통로인 칸 수
for i in range(N) :
    for j in range(N) :
        cnt = 0   # 현재 위치에서 주변의 통로 개수
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]] :
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N :
                if text[ni][nj] != '1' :
                    cnt += 1
        if cnt == 4 :
            ans += 1



