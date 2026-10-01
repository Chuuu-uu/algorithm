T = int(input())

# 등급
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, T + 1) :
    N, K = map(int, input().split())

    # 점수 저장할 빈 리스트
    score = []

    # 중간, 기말, 과제 점수 저장 후 총점 계산
    for i in range(N) :
        mid, fin, assi = list(map(int, input().split()))

        total = mid * 0.35 + fin * 0.45 + assi * 0.2

        # 총점 리스트에 저장
        score.append(total)

    # k번째 학생의 점수 저장
    kscore = score[K-1]

    # 내림차순 정렬
    score.sort(reverse = True)

    # K번째 학생 등수
    rank = score.index(kscore)

    # 한 학점당 학생 수
    stu_per_grade = N // 10

    # 학점 구하기
    grade = grades[rank // stu_per_grade]

    print(f'#{tc} {grade}')