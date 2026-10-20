user_input = input("Enter student marks separated by spaces: ")
marks = [float(x) for x in user_input.split()]

if not marks:
    print("No marks entered!")
else:
    total_students = len(marks)
    highest_marks = max(marks)
    lowest_marks = min(marks)
    average_marks = sum(marks) / total_students

    passed_students = [m for m in marks if m >= 40]
    failed_students = [m for m in marks if m < 40]
    passed_count = len(passed_students)
    failed_count = len(failed_students)

    pass_percentage = (passed_count / total_students) * 100
    sorted_marks = sorted(marks)

    grade_a = len([m for m in marks if m >= 90])
    grade_b = len([m for m in marks if 80 <= m <= 89])

    print("\n--- STUDENT EXAM ANALYSIS REPORT ---")
    print(f"Total Students: {total_students}")
    print(f"Highest Marks: {highest_marks}")
    print(f"Lowest Marks: {lowest_marks}")
    print(f"Average Marks: {average_marks}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print(f"Pass Percentage: {pass_percentage}%")
    print(f"Sorted Marks: {sorted_marks}")
    print(f"Grade A: {grade_a} Students")
    print(f"Grade B: {grade_b} Students")