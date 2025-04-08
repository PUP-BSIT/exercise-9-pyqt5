import os

'''
"ID" will be the key for storing the student's unique identifier.
"Name" will be the key for storing the student's name.
"Program" will be the key for storing the student's program of study.
"Grade" will be the key for storing the student's grade level.
"Section" will be the key for storing the student's class section.
student_id will be used for storing the student's unique identifier.
student_name will be used for storing the student's name.
student_program will be used for storing the student's program of study.
student_grade will be used for storing the student's grade level.
student_section will be used for storing the student's class section.
'''

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
    
    for student in student_data:
        for key, value in student.items():
            print(f"{key}: {value}")
                
def add_student_record(student_record):
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name (Surname, First Name M.I.): ")
    student_program = input("Enter Student Program: ")
    student_grade = input("Enter Student Grade: ")
    student_section = input("Enter Student Section: ")

    student_record.append({
        "ID": student_id,
        "Name": student_name,
        "Program": student_program,
        "Grade": student_grade,
        "Section": student_section,
    })
            
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
                add_student_record(student_data)
                buffer()
            
            case "3": 
                #TODO(ARGUELLES): Implement update function   
                pass
            
            case "4":
                #TODO(CONDINO): Implement delete function     
                pass
            
            case "5":
                #TODO(CAYA): Implement search function
                pass
            
            case "6":
                break
            
            case _:   
                print("Invalid Input.")  
                   
main_menu(student_data)