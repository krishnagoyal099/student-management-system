

# Student Management System

A Python-based **Student Management System** built using Object-Oriented Programming (OOP). This project allows you to manage student records, including adding, viewing, updating, deleting, and searching for students.

## Features

1. **Add Student**  
   Add a student with the following details:
   - Student ID
   - Name
   - Age
   - Grade

2. **View Students**  
   Display a list of all registered students.

3. **Update Student**  
   Update the details of an existing student.

4. **Delete Student**  
   Remove a student record from the system.

5. **Search Student**  
   Search for a student by their Student ID.

6. **Exit**  
   Quit the program gracefully.

## Technologies Used

- **Programming Language**: Python 3.x

## Installation and Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/student-management-system.git
   cd student-management-system
   ```

2. **Run the program**:
   ```bash
   python student_management.py
   ```

3. **Follow the menu**:  
   Interact with the system by entering the appropriate menu options.

## Sample Usage

### Menu
```
--- Student Management System ---
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Search Student
6. Exit
Enter your choice:
```

### Adding a Student
```plaintext
Enter Student ID: 101
Enter Student Name: Alice
Enter Student Age: 20
Enter Student Grade: A
Student added successfully!
```

### Viewing Students
```plaintext
--- Student List ---
ID: 101, Name: Alice, Age: 20, Grade: A
```

## Project Structure

```
.
├── student_management.py   # Main Python script
└── README.md               # Project documentation
```

## Future Enhancements

- Add a feature to save and load student records to/from a file.
- Integrate a graphical user interface (GUI) using Tkinter or PyQt.
- Add login authentication for administrators.


