# Initialising dictionary
student_grades = { }

#  Add a new student
def add_student(name, grade):
  student_grades[name] = grade
  print(f'Student {name} added with grade {grade}')

# Update a student
def update_student(name, new_grade):
  if name in student_grades:
    student_grades[name] = new_grade
    print(f'Student {name} updated with new grade {new_grade}') 
    
  else:
    print(f'Student {name} not found')

# Delete a student
def delete_student(name):
  if name in student_grades:
    del student_grades[name]
    print(f'Student {name} deleted')
    
  else:
    print(f'Student {name} not found')

# View all students
def view_students():
  if student_grades:
    for name, grade in student_grades.items():
      print(f'Stuent: {name} : {grade}')
            
  else:
    print('No students found')

# Main program loop
def main():
  while True:
    print('\nStudent Grades Management System')
    print('Press 1 to add a student')
    print('Press 2 to update a student')
    print('Press 3 to delete a student')
    print('Press 4 to view students')
    print('Press 5 to exit')

    choice = input("Enter your choice: ")
    if choice == '1':
      name = input('Enter student name: ')
      grade = int(input('Enter student grade: '))
      add_student(name, grade)

    elif choice == '2':
      name = input('Enter student name: ')
      new_grade = int(input('Enter new grade: '))
      update_student(name, new_grade)

    elif choice == '3':
      name = input('Enter student name: ')
      delete_student(name)

    elif choice == '4':
      view_students()

    elif choice == '5':
      print('Exiting the program')
      break

    else:
      print('Invalid choice. Please try again')

if __name__ == '__main__':
  main()
else:
  print('This is not the main file')