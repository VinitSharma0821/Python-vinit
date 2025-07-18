students = []
subjects_offered = ["Math", "Science", "English", "History", "Computer Science"]

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    students.append({
        "id": student_id,
        "name": name,
        "age": age
    })
    print("Student added successfully!\n")

def display_all_students():
    if not students:
        print("No students available.\n")
        return
    print("\nList of Students:")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}")
    print()

def update_student():
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s['id'] == sid:
            s['name'] = input("Enter new name: ")
            s['age'] = int(input("Enter new age: "))
            print("Student information updated!\n")
            return
    print("Student not found!\n")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    for i, s in enumerate(students):
        if s['id'] == sid:
            del students[i]
            print("Student deleted!\n")
            return
    print("Student not found!\n")

def display_subjects():
    print("\nSubjects Offered:")
    for sub in subjects_offered:
        print(f"- {sub}")
    print()

# Main loop
while True:
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = int(input("choose your option (1/2/3/4/5/6)"))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_all_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        display_subjects()
    elif choice == 6:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
