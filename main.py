import os

student_data = []

def clear_screen():
    windows_nt = "nt"
    os.system('cls' if os.name == windows_nt else 'clear')
    
def buffer():
    input("\nPress Enter to continue...")

def list_all_student_data(student_data):
    if not student_data:
        print("\nNo records to display.")
        return
    
    print("\n---------------Student Data----------------")
    for student in student_data:
        print(
            f"Name: {student['Name']}\n"
            f"ID: {student['ID']}\n" 
            f"Program: {student['Program']}\n"
            f"Grade and Section: {student['Grade']} - {student['Section']}"
        )
        print("-------------------------------------------")
                
def add_student_data(student_data):
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name (Ln, Fn M.I.): ")
    student_program = input("Enter Student Program: ")
    student_grade = input("Enter Student Grade: ")
    student_section = input("Enter Student Section: ")

    student_data.append({
        "ID": student_id,
        "Name": student_name,
        "Program": student_program,
        "Grade": student_grade,
        "Section": student_section,
    })

def update_student_data(student_data):
    if not student_data:
        print("\nNo records to update.")
        return

    student_id = input("Enter Student ID: ")

    print("\n--------------------------------------------------------\n")

    for student in student_data:
        if student["ID"] == student_id:
            student["ID"] = input("Update Student ID: ")
            student["Name"] = input("Update Student Name (Ln, Fn M.I.): ")
            student["Program"] = input("Update Student Program: ")
            student["Grade"] = input("Update Student Grade: ")
            student["Section"] = input("Update Student Section: ")
            return
        
    print(f"Student ID {student_id} not found.")

def delete_student_data(student_data):
    if not student_data:
        print("\nNo records to delete.")
        return
    
    delete_student_id = input("Enter Student ID: ")
    
    for student in student_data:
        if student["ID"] == delete_student_id:
            student_data.remove(student)  
            print(f"Student ID {delete_student_id} has been deleted.")
            return
        
    print(f"Student ID {delete_student_id} not found.")
    
def print_specific_data(student):
    for key, value in student.items():
        print(f"{key}: {value}") 

def search_student_data(student_data):
    if not student_data:
        print("\nNo records to search.")
        return
    
    search_student_id = input("Enter Student ID to search: ")
    
    for student in student_data:
        if student["ID"] == search_student_id:
            print(f"Student ID {search_student_id} has been found.\n")
            print_specific_data(student)
            return
        
    print(f"Student ID {search_student_id} not found.")
            
def main_menu(student_data):
    choice = ""
    
    while choice != "6":
        clear_screen()
        print("--Main Menu Student Record--")
        print("\n1. List All")
        print("2. Add")
        print("3. Update")
        print("4. Delete")
        print("5. Search")
        print("6. Exit")
        
        choice = input("\nEnter your choice: ")
        
        clear_screen()
        
        match choice:
            case "1":   
                list_all_student_data(student_data)
                buffer()
                
            case "2":  
                add_student_data(student_data)
                buffer()
            
            case "3": 
                update_student_data(student_data) 
                buffer()
            
            case "4":
                delete_student_data(student_data)    
                buffer()
            
            case "5":
                search_student_data(student_data)
                buffer()
            
            case "6":
                break
            
            case _:   
                print("Invalid Input.")  
                   
main_menu(student_data)