def calculate_new_score(score):
    multiples = round(score / 5) * 5
    if(multiples < 40):
        return score
    elif((multiples - score) <= 3):
        return multiples
    else:
        pass

student_scores = {"德瑞克": 33, "尚恩": 73, "傑夫": 63, "馬基": 39}
student_new_scores = {}
for student, score in student_scores.items():
    new_score = calculate_new_score(score)
    student_new_scores[student] = new_score

for student, score in student_new_scores.items():
    print("{} {}".format(student, score))
