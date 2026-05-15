n = int(input())

common_courses = set(input().split())

for _ in range(n - 1):
    student_courses = set(input().split())
    common_courses.intersection_update(student_courses)

print(len(common_courses))
