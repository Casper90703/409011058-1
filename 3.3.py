total_students = 0
pass_students = 0
fail_students = 0
total_score = 0


while True:
    score = float(input("請輸入學生成績（輸入-1表示結束）："))
    
   
    if score == -1:
        break
    

    total_students += 1
    total_score += score
    

    if score >= 60:
        pass_students += 1
    else:
        fail_students += 1


if total_students > 0:
    average_score = total_score / total_students
else:
    average_score = 0

print("全班人數：", total_students)
print("及格人數：", pass_students)
print("不及格人數：", fail_students)
print("全班平均值：", average_score)
