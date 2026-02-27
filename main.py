from utils import *

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    try:
        marks = []
        for i in range(1, 6):
            mark = float(input(f"Enter marks for subject {i}: "))
            marks.append(mark)
    except ValueError:
        print("Invalid marks entered! Try again.")
        return

    total, percentage, grade = calculate_result(marks)

    student_record = f"{roll},{name},{marks},{total},{percentage:.2f},{grade}"
    save_student(student_record)

    print("Student record added successfully!")


def view_students():
    students = read_students()
    if not students:
        print("No records found.")
        return

    print("\n--- Student Records ---")
    print("-" * 60)

    for student in students:
        roll, name, marks, total, percentage, grade = student.strip().split(",")

        print(f"Roll No     : {roll}")
        print(f"Name        : {name}")
        print(f"Marks       : {marks}")
        print(f"Total Marks : {total}")
        print(f"Percentage  : {percentage}%")
        print(f"Grade       : {grade}")
        print("-" * 60)


def search_student():
    roll_search = input("Enter roll number to search: ")
    students = read_students()

    found = False
    for student in students:
        if student.startswith(roll_search + ","):
            print("Record Found:")
            print(student.strip())
            found = True
            break

    if not found:
        print("Student not found.")


def delete_student():
    roll_delete = input("Enter roll number to delete: ")
    students = read_students()
    new_list = []

    found = False
    for student in students:
        if not student.startswith(roll_delete + ","):
            new_list.append(student)
        else:
            found = True

    overwrite_students(new_list)

    if found:
        print("Record deleted successfully.")
    else:
        print("Student not found.")


def menu():
    while True:
        print("\n===== Student Result Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    menu()
