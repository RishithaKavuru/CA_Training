#Q3
Physics = int(input())
Chemistry = int(input())
Biology = int(input())
Mathematics = int(input())
Computer = int(input())

total_marks = Physics + Chemistry + Biology + Mathematics + Computer
percentage = (total_marks/500) * 100

def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"

grade = get_grade(percentage)
print(f"Percentage: {percentage} & Grade: {grade}")

