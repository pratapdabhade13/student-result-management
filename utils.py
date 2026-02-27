import os

FILE_NAME = "data.txt"

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)
    grade = calculate_grade(percentage)
    return total, percentage, grade


def save_student(student_data):
    with open(FILE_NAME, "a") as file:
        file.write(student_data + "\n")


def read_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return file.readlines()


def overwrite_students(all_students):
    with open(FILE_NAME, "w") as file:
        file.writelines(all_students)
