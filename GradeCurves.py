
# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

highest_score = 0
top_student = None
top_grade_pct = 0

for name, scores in student_grades.items():
    total_points = sum(scores)
    if total_points > highest_score:
        highest_score = total_points
        top_student = name
        top_grade_pct = total_points / 5

print(f'The student with the highest total of points is {top_student}.\n')
print(f'GPA of {top_student}: %{top_grade_pct:.1f}')

print('\nAssignment Averages:')
avg_scores = [sum(assignment) / len(assignment) for assignment in zip(*student_grades.values())]
for assignment, score in enumerate(avg_scores, start=1):
    print(f'Assignment {assignment}: %{score:.2f}')

best_total = highest_score
curved_grades = {}

for name, scores in student_grades.items():
    total_points = sum(scores)
    curved_total = (total_points / best_total) * 100
    curved_grades[name] = curved_total

print('\nTotal after calculating curve:')
for name, curved_total in curved_grades.items():
    print(f'{name}: %{curved_total:.2f}')
