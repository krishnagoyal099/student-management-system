class Student:
    def __init__(self, sid, name, age, grade):
        self.sid = sid  # Student ID
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.sid}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, sid, name, age, grade):
        if sid in self.students:
            print(f"Student with ID {sid} already exists!")
        else:
            self.students[sid] = Student(sid, name, age, grade)
            print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found!")
        else:
            print("\n--- Student List ---")
            for student in self.students.values():
                print(student)

    def update_student(self, sid, name=None, age=None, grade=None):
        if sid not in self.students:
            print(f"No student found with ID {sid}.")
        else:
            student = self.students[sid]
            if name:
                student.name = name
            if age:
                student.age = age
            if grade:
                student.grade = grade
            print("Student updated successfully!")

    def delete_student(self, sid):
        if sid in self.students:
            del self.students[sid]
            print(f"Student with ID {sid} deleted successfully!")
        else:
            print(f"No student found with ID {sid}.")

    def search_student(self, sid):
        if sid in self.students:
            print("\n--- Student Found ---")
            print(self.students[sid])
        else:
            print(f"No student found with ID {sid}.")


def main():
    system = StudentManagementSystem()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            grade = input("Enter Student Grade: ")
            system.add_student(sid, name, age, grade)

        elif choice == "2":
            system.view_students()

        elif choice == "3":
            sid = input("Enter Student ID to update: ")
            print("Leave fields blank to skip updating.")
            name = input("Enter new Name (or press Enter to skip): ")
            age = input("Enter new Age (or press Enter to skip): ")
            grade = input("Enter new Grade (or press Enter to skip): ")
            system.update_student(
                sid,
                name=name if name else None,
                age=int(age) if age.isdigit() else None,
                grade=grade if grade else None,
            )

        elif choice == "4":
            sid = input("Enter Student ID to delete: ")
            system.delete_student(sid)

        elif choice == "5":
            sid = input("Enter Student ID to search: ")
            system.search_student(sid)

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
