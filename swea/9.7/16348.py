T = int(input())

for tc in range(1, T + 1):
    # N: 한 줄의 길이
    # M: 찾아야 하는 회문의 길이
    N, M = map(int, input().split())

    # N개의 문자열 입력
    text = [input() for _ in range(N)]

    answer = ""

    # i: 행 또는 열 번호
    for i in range(N):
        # 회문의 시작 위치
        for j in range(N - M + 1):

            # 가로 방향 회문 판별
            for k in range(M // 2):
                if text[i][j + k] != text[i][j + M - 1 - k]:
                    break
            else:
                answer = text[i][j:j + M]

            # 세로 방향 회문 판별
            for k in range(M // 2):
                if text[j + k][i] != text[j + M - 1 - k][i]:
                    break
            else:
                answer = ""
                for k in range(M):
                    answer += text[j + k][i]

    print(f"#{tc} {answer}")



# # 회문인지 판단하는 방법
# # 맨앞/맨뒤 같은지 비교
# # 맨앞 + 1/맨뒤 - 1 같은지 비교
# # .....
# # 문자열길이/2만큼 반복
# # 중간에 다른적이 한번이라도 있다면? => 회문이 아니다.
# answer = True  # 회문이다로 가정
#
#
# # 반복 비교를 N//2만큼, 비교 횟수를 k
# for k in range(N//2) :
#     # k를 가지고 앞쪽 인덱스, 뒤쪽 인덱스 나타내보기
#     # 앞쪽 인덱스는 비교하면서 +1씩 증가
#     # 뒤쪽 인덱스는 비교하면서 -1씩 감소
#     # 앞쪽과 뒤쪽이 다르면
#     if string1[k] != string1[N-1-k] :
#         # 회문이 아님
#         answer = False
# print(answer)