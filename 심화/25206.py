# 너의 평점(학점)

Rating = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0}
Total = 0
Result = 0

for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
    if(grade != "P"):
        Total += credit
        Result += credit * Rating[grade]

print("%.6f" % (Result / Total))