# 학점 당 점수에 대한 매핑 표 먼저 만든 후 20줄 동안 과목명, 성적, 등급을 입력받고 평점 내기
# 패논패 과목은 점수 계산 대상에서 제외(예외 조건)
# gpa = 학점 * 평점 총합 / 학점 총합

grade_to_score = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F":  0.0
}

total_score = 0.0
total_credits = 0.0

for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)

    if grade == "P":
        continue

    total_score += credit * grade_to_score[grade]
    total_credits += credit

if total_credits == 0:
    print("0.000000")       # 20개 전공 성적이 빵점일 때
else:
    gpa = total_score / total_credits
    print(f"{gpa:0.6f}")