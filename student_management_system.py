import sqlite3

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    if choice == 1:

        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        marks = int(input("Enter Student Marks: "))

        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?)",
            (sid, name, marks)
        )

        conn.commit()
        print("Student added successfully.")

    elif choice == 2:

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        if len(students) == 0:
            print("No records found.")
        else:
            print("\nStudent Records")
            for student in students:
                print("Student ID :", student[0])
                print("Name       :", student[1])
                print("Marks      :", student[2])
                print("---------------------------")

    elif choice == 3:

        sid = input("Enter Student ID to Search: ")

        cursor.execute("SELECT * FROM students WHERE sid = ?", (sid,))
        student = cursor.fetchone()

        if student:
            print("Student ID :", student[0])
            print("Name       :", student[1])
            print("Marks      :", student[2])
        else:
            print("Student not found.")

    elif choice == 4:

        sid = input("Enter Student ID to Update: ")

        cursor.execute("SELECT * FROM students WHERE sid = ?", (sid,))
        student = cursor.fetchone()

        if student:

            name = input("Enter New Name: ")
            marks = int(input("Enter New Marks: "))

            cursor.execute(
                "UPDATE students SET name=?, marks=? WHERE sid=?",
                (name, marks, sid)
            )

            conn.commit()
            print("Student updated successfully.")

        else:
            print("Student not found.")

    elif choice == 5:

        sid = input("Enter Student ID to Delete: ")

        cursor.execute("SELECT * FROM students WHERE sid = ?", (sid,))
        student = cursor.fetchone()

        if student:

            cursor.execute("DELETE FROM students WHERE sid = ?", (sid,))
            conn.commit()

            print("Student deleted successfully.")

        else:
            print("Student not found.")

    elif choice == 6:

        conn.close()
        print("Thank you.")
        break

    else:
        print("Invalid Choice")

    conn.close()
