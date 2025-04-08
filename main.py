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
                pass
                
            case "2":   
                pass
            
            case "3":    
                pass
            
            case "4":     
                pass
            
            case "5":
                pass
            
            case "6":
                break
            
            case _:   
                print("Invalid Input.")  
                   
main_menu(student_data)