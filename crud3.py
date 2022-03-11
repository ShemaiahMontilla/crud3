"""
Elements :- ['Name',                 'Id Number', 'Year Level', 'Gender', 'Course']
1. Display list of students
2. Add new students
3. Edit student
4. Delete a student
5. Search a student by id number
6. Quit
"""

import csv
# Define global variables
student_elements = ['Name','Id Number', 'Year Level', 'Gender', 'Course']
student_database = 'Student_Data.csv'


def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Information System")
    print("---------------------------------------")
    print("A. Display list of students")
    print("B. Add new students")
    print("C. Edit student")
    print("D. Delete a student")
    print("E.  Search a student by id number (YYYY-NNNN) e.g. 2021-0001")
    print("F. Quit")

def display_students():
    global student_elements
    global student_database

    print("--- Student Records ---")

    with open(student_database, "r", encoding="utf-8") as g:
        reader = csv.reader(g)
        for x in student_elements:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("PRESS ANY KEY TO CONTINUE")


def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_elements
    global student_database

    # [ ['1','2'] ]
    student_data = []
    for element in student_elements:
        value = input("Enter " + element + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as g:
        writer = csv.writer(g)
        writer.writerows([student_data])

    print("DATA ADDED SUCCESSFULLY")
    input("PRESS ANY KEY TO CONTINUE")
    return

def update_student():
    global student_elements
    global student_database

    print("--- Update Student ---")
    id_number = input("Enter id number (YYYY-NNNN) e.g. 2021-0001 to update: ")
    index_student = None
    updated_student_data = []
    with open(student_database, "r", encoding="utf-8") as g:
        reader = csv.reader(g)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if id_number == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for element in student_elements:
                        value = input("Enter " + element + ": ")
                        student_data.append(value)
                    updated_student_data.append(student_data)
                else:
                    updated_student_data.append(row)
                counter += 1


    # Check if the record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as g:
            writer = csv.writer(g)
            writer.writerows(updated_student_data)
    else:
        print("ID NUMBER NOT FOUND IN OUR DATABASE")

    input("PRESS ANY KEY TO CONTINUE")


def delete_student():
    global student_elements
    global student_database

    print("--- Delete Student ---")
    id_number = input("Enter id number (YYYY-NNNN) e.g. 2021-0001 to delete: ")
    student_found = False
    updated_student_data = []
    with open(student_database, "r", encoding="utf-8") as g:
        reader = csv.reader(g)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if id_number != row[0]:
                    updated_student_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as g:
            writer = csv.writer(g)
            writer.writerows(updated_student_data)
        print("Student  ", id_number, "deleted successfully")
    else:
        print("ID NUMBER NOT FOUND IN OUR DATABASE")

    input("PRESS ANY KEY TO CONTINUE")


def search_student():
    global student_elements
    global student_database

    print("--- Search Student ---")
    id_number = input("Enter id number (YYYY-NNNN) e.g. 2021-0001 to search: ")
    with open(student_database, "r", encoding="utf-8") as g:
        reader = csv.reader(g)
        for row in reader:
            if len(row) > 0:
                if id_number == row[0]:
                    print("----- Student Found -----")
                    print("Name: ", row[0])
                    print("Id Number: ", row[1])
                    print("Year Level: ", row[2])
                    print("Gender: ", row[3])
                    print("Course: ", row[4])
                    break
        else:
            print("ID NUMBER NOT FOUND IN OUR DATABASE")
    input("PRESS ANY KEY TO CONTINUE")




while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == 'A':
        display_students()
    elif choice == 'B':
        add_student()
    elif choice == 'C':
        update_student()
    elif choice == 'D':
        delete_student()
    elif choice == 'E':
        search_student()
    else:
        break

print("-------------------------------")
print(" THANK YOU FOR USING OUR SYSTEM")
print("-------------------------------")