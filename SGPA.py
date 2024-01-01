import sys

#Clear Screen
def clear():
    from os import name, system
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#Wait for user keypress
def keypress():
    input("Press 'ENTER' to continue...")

#Course Menu
def course_menu():
    from time import sleep
    clear()
    while True:
        Course_Menu_Banner(2019)
        choice = int(input("  Enter your choice:"))
        if choice == 1:
            BCA_Sem_Menu()
        elif choice == 2:
            BA_Sem_Menu()
        elif choice == 3:
            print('Not Available')
            keypress()
            clear()
        elif choice == 4:
            print('Not Available')
            keypress()
            clear()
        elif choice == 5:
            clear()
            exit()
        else: 
            print("Invalid choice")
            sleep(2)
            clear()

#Repetation
def rep():
    ans = input("Do you want to go back to the main menu(Y/N):")
    if ans == 'y' or ans =='Y':
        course_menu()
    else:
        exit(0)

#Grading
def Grades(per):
    grade = ''
    clear()
    if per >= 90 and per <=100:
        grade = 'O'
    elif per >= 80 and per <= 89.99:
        grade = 'A++'
    elif per >= 70 and per <= 79.99:
        grade = 'A+'
    elif per >= 60 and per <= 69.99:
        grade = 'A'
    elif per >= 55 and per <= 59.99:
        grade = 'B+'
    elif per >= 50 and per <= 54.99:
        grade = 'B'
    elif per >= 40 and per <= 49.99:
        grade = 'C'
    elif per > 0 and per < 40:
        grade = 'F'
    else:
        print("Error: Invalid Percentage!")
    return grade

#Final Output
def final_output(total_marks_obtained,total_marks,per,total_grade_points,mm,yy,grade,sgpa):
    print("\n\033[1m /------------------------------------------------------------------------\\\033[0m")
    print('\033[1m\tTO\tTM\tPer(%)\tTGPA\tGrade\tSGPA\tMonth\tYear\033[0m')
    print('\033[1m|------------|-------|--------|-------|-------|------|--------|------------|\033[0m')
    print(f'\t{total_marks_obtained}\t{total_marks}\t{round(per,2)}\t {int(total_grade_points)}\t {grade}\t{round(sgpa,2)}\t{mm}\t{yy}')
    print("\033[1m \\------------------------------------------------------------------------/\n\033[0m")

#Marks Input and Credit Score Validation
max_attempts = 3
def get_marks(subject, min_marks, max_marks,course,sem):
    attempts = 0
    while attempts < max_attempts:
        attempts = attempts + 1
        clear()
        print(f'Attempt {attempts} out of 3         {course} - Semester - {sem}')
        print('------------------------------------------------------')
        marks = input(f'Enter marks for {subject} between {min_marks} and {max_marks}:')
        marks = validate(marks, min_marks, max_marks)
        if not marks:
            clear()
            print(f'Attempt {attempts} out of 3         {course} - Semester - {sem}')
            print('------------------------------------------------------')
            print(f'Marks for {subject} must be a number between {min_marks} and {max_marks}\n\tPress ENTER to continue...')
            input()
        else:
            return marks
    clear()
    print(f'Attempt {attempts} out of 3         {course} - Semester - {sem}')
    print('------------------------------------------------------')
    print('You have exceeded max attempts. Program terminated...')
    sys.exit()
def validate(marks, min_marks, max_marks):
    if marks.isdigit():
        marks = int(marks)
        if min_marks <= marks <= max_marks:
            return marks
    return None
def get_credits(subject, min_marks, max_marks,course,sem):
    attempts = 0
    while attempts < max_attempts:
        attempts = attempts + 1
        clear()
        print(f'Attempt {attempts} out of 3         {course} - Semester - {sem}')
        print('------------------------------------------------------')
        marks = input(f'Enter credits for {subject} between {min_marks} and {max_marks}:')
        marks = validate(marks, min_marks, max_marks)
        if not marks:
            clear()
            print(f'Attempt {attempts} out of 3         {course} - Semester - {sem}')
            print('------------------------------------------------------')
            print(f'Credits for {subject} must be a number between {min_marks} and {max_marks}\n\tPress ENTER to continue...')
            input()
        else:
            return marks
    clear()
    print(f'Attempt {attempts} out of 3         {course} - Semester - {sem}')
    print('------------------------------------------------------')
    print('You have exceeded max attempts. Program terminated...')
    sys.exit()


#Grade Points
def grade_points_assigment(marks,max_marks):
    if max_marks == 100:
        grade_points = 0.0
        if 96 <= marks <= 100:
            grade_points = 10
        elif 91 <= marks <= 95:
            grade_points = 9.5
        elif 86 <= marks <= 90:
            grade_points = 9
        elif 81 <= marks <= 85:
            grade_points = 8.5
        elif 76 <= marks <= 80:
            grade_points = 8
        elif 71 <= marks <= 75:
            grade_points = 7.5
        elif 66 <= marks <= 70:
            grade_points = 7
        elif 61 <= marks <= 65:
            grade_points = 6.5
        elif 56 <= marks <= 60:
            grade_points = 6
        elif 51 <= marks <= 55:
            grade_points = 5.5
        elif 46 <= marks <= 50:
            grade_points = 5
        elif 41 <= marks <= 45:
            grade_points = 4.5
        elif 35 <= marks <= 40:
            grade_points = 4
        return grade_points
    elif max_marks == 50:
        grade_points = 0.0
        if 48 <= marks <= 50:
            grade_points = 10
        elif 46 <= marks <= 47:
            grade_points = 9.5
        elif 43 <= marks <= 45:
            grade_points = 9
        elif 41 <= marks <= 42:
            grade_points = 8.5
        elif 38 <= marks <= 40:
            grade_points = 8
        elif 36 <= marks <= 37:
            grade_points = 7.5
        elif 33 <= marks <= 35:
            grade_points = 7
        elif 31 <= marks <= 32:
            grade_points = 6.5
        elif 28 <= marks <= 30:
            grade_points = 6
        elif 26 <= marks <= 27:
            grade_points = 5.5
        elif 23 <= marks <= 25:
            grade_points = 5
        elif 21 <= marks <= 22:
            grade_points = 4.5
        elif 18 <= marks <= 20:
            grade_points = 4
        return grade_points

#Course Menu Banner
def Course_Menu_Banner(batch):
    clear()
    print(f"\033[1m \t\t   Batch - {batch}  \n\t\t   Course Menu \033[0m")
    print("  /-----------------------------------------------\\")
    print(" |  1.BCA        |  2.BA          |  3.BSc         |\n |---------------|----------------|----------------|\n |  4.Bcom       |  5.Quit        |                |")  
    print("  \\-----------------------------------------------/")

#Sem Menu Banner
def Sem_Menu_Banner(course,batch):
    clear()
    print(f"\033[1m   Batch - {batch}   |  Semester Menu  |   Course - {course} \033[0m")
    print(" /---------------------------------------------------\\")
    print("|  [1]Semester-1  |  [2]Semester-2  |  [3]Semester-3  |\n|-----------------|-----------------|-----------------|\n|  [4]Semester-4  |  [5]Semester-5  |  [6]Semester-6  |\n|-----------------|-----------------|-----------------|\n|  [7]Course Menu |  [8]Quit        |                 |")  
    print(" \\---------------------------------------------------/")

#Sem Banner
def Sem_Banner(course,sem):
    clear()
    print("/------------------------------------------------------\\")
    print(f"\033[1m \t\t    {course} - Semester - {sem} \033[0m")
    print("\\------------------------------------------------------/")



#BA 2019
def BA_Sem_Menu():
    clear()
    while True:
        Sem_Menu_Banner('BA',2019)
        choice = int(input("  Enter your choice:"))

        if choice == 1:
            BA_Sem_1()
            rep()
        elif choice == 2:
            BA_Sem_2()
            rep()
        elif choice == 3:
            BA_Sem_3()
            rep()
        elif choice == 4:
            BA_Sem_4()
            rep()
        elif choice == 5:
            BA_Sem_5()
            rep()
        elif choice == 6:
            BA_Sem_6()
            rep()
        elif choice == 7:
            course_menu()
        elif choice == 8:
            exit()
        else:
            print("Invalid choice, Please select from the given options")
            keypress()
            clear()

def BA_Sem_1():
    month = 'Nov'
    year = 2019

    m1 = get_marks('English',35,100,'BA',1)
    g1 = grade_points_assigment(m1,100)
    c1 = get_credits('English',1,5,'BA',1)

    m2 = get_marks('K/S/H',35,100,'BA',1)
    g2 = grade_points_assigment(m2,100)
    c2 = get_credits('K/S/H',1,5,'BA',1)

    m3 = get_marks('Sociology',35,100,'BA',1)
    g3 = grade_points_assigment(m3,100)
    c3 = get_credits('Sociology',1,5,'BA',1)

    m4 = get_marks('Economics',35,100,'BA',1)
    g4 = grade_points_assigment(m4,100)
    c4 = get_credits('Economics',1,5,'BA',1)

    m5 = get_marks('Optional Kannada',35,100,'BA',1)
    g5 = grade_points_assigment(m5,100)
    c5 = get_credits('Optional Kannada',1,5,'BA',1)

    m6 = get_marks('Indian Constitution and Human Rights',35,100,'BA',1)
    g6 = grade_points_assigment(m6,100)
    c6 = get_credits('Indian Constitution and Human Rights',1,5,'BA',1)

    total_marks_obtained = m1+m2+m3+m4+m5+m6
    total_marks = 600
    percentage = total_marks_obtained / total_marks * 100
    total_credits_obtained = c1+c2+c3+c4+c5+c6
    total_grade_points_obtained = g1+g2+g3+g4+g5+g6
    total_credit_points = (c1*g1) + (c2*g2) + (c3*g3) + (c4*g4) + (c5*g5) + (c6*g6)
    sgpa = total_credit_points / total_credits_obtained
    grade = Grades(percentage)
    final_output(total_marks_obtained,total_marks,percentage,total_grade_points_obtained,month,year,grade,sgpa)

def BA_Sem_2():
    month = 'Sept' 
    year = 2020

    m1 = get_marks('English',35,100,'BA',2)
    g1 = grade_points_assigment(m1,100)
    c1 = get_credits('English',1,5,'BA',2)

    m2 = get_marks('K/S/H',35,100,'BA',2)
    g2 = grade_points_assigment(m2,100)
    c2 = get_credits('K/S/H',1,5,'BA',2)

    m3 = get_marks('Sociology',35,100,'BA',2)
    g3 = grade_points_assigment(m3,100)
    c3 = get_credits('Sociology',1,5,'BA',2)

    m4 = get_marks('Economics',35,100,'BA',2)
    g4 = grade_points_assigment(m4,100)
    c4 = get_credits('Economics',1,5,'BA',2)

    m5 = get_marks('Optional Kannada',35,100,'BA',2)
    g5 = grade_points_assigment(m5,100)
    c5 = get_credits('Optional Kannada',1,5,'BA',2)

    m6 = get_marks('Computer Application and IT',35,100,'BA',2)
    g6 = grade_points_assigment(m6,100)
    c6 = get_credits('Computer Application and IT',1,5,'BA',2)

    m7 = get_marks('Computer Application and IT - Lab',18,50,'BA',2)
    g7 = grade_points_assigment(m7,50)
    c7 = get_credits('English',1,5,'BA',2)
    
    total_marks_obtained = m1+m2+m3+m4+m5+m6+m7
    total_marks = 650
    percentage = total_marks_obtained / total_marks * 100
    total_credits_obtained = c1+c2+c3+c4+c5+c6+c7
    total_grade_points_obtained = g1+g2+g3+g4+g5+g6+g7
    total_credit_points = (c1*g1) + (c2*g2) + (c3*g3) + (c4*g4) + (c5*g5) + (c6*g6) + (c7*g7)
    sgpa = total_credit_points / total_credits_obtained
    grade = Grades(percentage)
    final_output(total_marks_obtained,total_marks,percentage,total_grade_points_obtained,month,year,grade,sgpa)

def BA_Sem_3():
    month = 'Mar' 
    year = 2021
    m1 = get_marks('English',35,100,'BA',3)
    g1 = grade_points_assigment(m1,100)
    c1 = get_credits('English',1,5,'BA',3)

    m2 = get_marks('K/S/H',35,100,'BA',3)
    g2 = grade_points_assigment(m2,100)
    c2 = get_credits('K/S/H',1,5,'BA',3)

    m3 = get_marks('Sociology',35,100,'BA',3)
    g3 = grade_points_assigment(m3,100)
    c3 = get_credits('Sociology',1,5,'BA',3)

    m4 = get_marks('Economics',35,100,'BA',3)
    g4 = grade_points_assigment(m4,100)
    c4 = get_credits('Economics',1,5,'BA',3)

    m5 = get_marks('Optional Kannada',35,100,'BA',3)
    g5 = grade_points_assigment(m5,100)
    c5 = get_credits('Optional Kannada',1,5,'BA',3)

    m6 = get_marks('Value Education',18,50,'BA',3)
    g6 = grade_points_assigment(m6,50)
    c6 = get_credits('Value Education',1,5,'BA',3)

    m7 = get_marks('Open Elective: Physics in Daily Life',18,50,'BA',3)
    g7 = grade_points_assigment(m7,50)
    c7 = get_credits('Open Elective: Physics in Daily Life',1,5,'BA',3)

    total_marks_obtained = m1+m2+m3+m4+m5+m6+m7
    total_marks = 600
    percentage = total_marks_obtained / total_marks * 100
    total_credits_obtained = c1+c2+c3+c4+c5+c6+c7
    total_grade_points_obtained = g1+g2+g3+g4+g5+g6+g7
    total_credit_points = (c1*g1) + (c2*g2) + (c3*g3) + (c4*g4) + (c5*g5) + (c6*g6) + (c7*g7)
    sgpa = total_credit_points / total_credits_obtained
    grade = Grades(percentage)
    final_output(total_marks_obtained,total_marks,percentage,total_grade_points_obtained,month,year,grade,sgpa)

def BA_Sem_4():
    month = 'Aug'
    year = 2021
    m1 = get_marks('English',35,100,'BA',4)
    g1 = grade_points_assigment(m1,100)
    c1 = get_credits('English',1,5,'BA',4)

    m2 = get_marks('K/S/H',35,100,'BA',4)
    g2 = grade_points_assigment(m2,100)
    c2 = get_credits('K/S/H',1,5,'BA',4)

    m3 = get_marks('Sociology',35,100,'BA',4)
    g3 = grade_points_assigment(m3,100)
    c3 = get_credits('Sociology',1,5,'BA',4)

    m4 = get_marks('Economics',35,100,'BA',4)
    g4 = grade_points_assigment(m4,100)
    c4 = get_credits('Economics',1,5,'BA',4)

    m5 = get_marks('Optional Kannada',35,100,'BA',4)
    g5 = grade_points_assigment(m5,100)
    c5 = get_credits('Optional Kannada',1,5,'BA',4)

    m6 = get_marks('Human Resource Management',18,50,'BA',4)
    g6 = grade_points_assigment(m6,50)
    c6 = get_credits('Human Resource Management',1,5,'BA',4)

    g7 = 1
    c7 = get_credits('Skill Development',1,5,'BA',4)

    total_marks_obtained = m1+m2+m3+m4+m5+m6
    total_marks = 550
    percentage = total_marks_obtained / total_marks * 100
    total_credits_obtained = c1+c2+c3+c4+c5+c6+c7
    total_grade_points_obtained = g1+g2+g3+g4+g5+g6+g7
    total_credit_points = (c1*g1) + (c2*g2) + (c3*g3) + (c4*g4) + (c5*g5) + (c6*g6) + (c7*g7)
    sgpa = total_credit_points / total_credits_obtained
    grade = Grades(percentage)
    final_output(total_marks_obtained,total_marks,percentage,total_grade_points_obtained,month,year,grade,sgpa)

def BA_Sem_5():
    month = 'March' 
    year = 2022
    m1 = get_marks('Sociology Paper V',35,100,'BA',5)
    g1 = grade_points_assigment(m1,100)
    c1 = get_credits('Sociology Paper V',1,5,'BA',5)

    m2 = get_marks('Sociology Paper VI: Sociology of Education',35,100,'BA',5)
    g2 = grade_points_assigment(m2,100)
    c2 = get_credits('Sociology Paper VI: Sociology of Education',1,5,'BA',5)

    m3 = get_marks('Economics Paper V',35,100,'BA',5)
    g3 = grade_points_assigment(m3,100)
    c3 = get_credits('Economics Paper V',1,5,'BA',5)

    m4 = get_marks('Economics Paper VI',35,100,'BA',5)
    g4 = grade_points_assigment(m4,100)
    c4 = get_credits('Economics Paper VI',1,5,'BA',5)

    m5 = get_marks('Optional Kannada Paper V',35,100,'BA',5)
    g5 = grade_points_assigment(m5,100)
    c5 = get_credits('Optional Kannada Paper V',1,5,'BA',5)

    m6 = get_marks('Optional Kannada Paper VI',35,100,'BA',5)
    g6 = grade_points_assigment(m6,100)
    c6 = get_credits('Optional Kannada Paper VI',1,5,'BA',5)

    m7 = get_marks('Enviornmental Science',18,500,'BA',5)
    g7 = grade_points_assigment(m7,50)
    c7 = get_credits('Enviornmental Science',1,5,'BA',5)

    m8 = get_marks('Seminar I:Kannada',18,50,'BA',5)
    g8 = grade_points_assigment(m8,50)
    c8 = get_credits('Seminar I:Kannada',1,5,'BA',5)

    m9 = get_marks('Seminar II:Sociology',18,50,'BA',5)
    g9 = grade_points_assigment(m9,50)
    c9 = get_credits('Seminar II:Sociology',1,5,'BA',5)

    total_marks_obtained = m1+m2+m3+m4+m5+m6+m7+m8+m9
    total_marks = 750
    percentage = total_marks_obtained / total_marks * 100
    total_credits_obtained = c1+c2+c3+c4+c5+c6+c7+c8+c9
    total_grade_points_obtained = g1+g2+g3+g4+g5+g6+g7+g8+g9
    total_credit_points = (c1*g1) + (c2*g2) + (c3*g3) + (c4*g4) + (c5*g5) + (c6*g6) + (c7*g7) + (c8*g8) + (c9*g9)
    sgpa = total_credit_points / total_credits_obtained
    grade = Grades(percentage)
    final_output(total_marks_obtained,total_marks,percentage,total_grade_points_obtained,month,year,grade,sgpa)

def BA_Sem_6():
    print('Not Available')
    keypress()


#BCA 2019
def BCA_Sem_Menu():
    clear()
    while True:
        Sem_Menu_Banner('BCA',2019)
        choice = int(input("  Enter your choice:"))
        if choice == 1:
            BCA_Sem_1()
            rep()
        elif choice == 2:
            BCA_Sem_2()
            rep()
        elif choice == 3:
            BCA_Sem_3()
            rep()
        elif choice == 4:
            BCA_Sem_4()
            rep()
        elif choice == 5:
            BCA_Sem_5()
            rep()
        elif choice == 6:
            BCA_Sem_6()
            rep()
            clear()
        elif choice == 7:
            course_menu()
        elif choice == 8:
            exit()
        else:
            print("Invalid choice, Please select from the given options")
            keypress()
            clear()

def BCA_Sem_1():
    month = 'Nov'
    year = 2019
    m1 = get_marks('English',35,100,'BCA',1)
    g1 = grade_points_assigment(m1,100)
    c1 = get_credits('English',1,6,'BCA',1)

    m2 = get_marks('K/S/H',35,100,'BCA',1)
    g2 = grade_points_assigment(m2,100)
    c2 = get_credits('K/S/H',1,6,'BCA',1)

    m3 = get_marks('Programming in C',35,100,'BCA',1)
    g3 = grade_points_assigment(m3,100)
    c3 = get_credits('Programming in C',1,6,'BCA',1)

    m4 = get_marks('Computer Organization And Architecture',35,100,'BCA',1)
    g4 = grade_points_assigment(m4,100)
    c4 = get_credits('Computer Organization And Architecture',1,6,'BCA',1)

    m5 = get_marks('Mathematics',35,100,'BCA',1)
    g5 = grade_points_assigment(m5,100)
    c5 = get_credits('Mathematics',1,6,'BCA',1)

    m6 = get_marks('Fundamentals Of Accounting',35,100,'BCA',1)
    g6 = grade_points_assigment(m6,100)
    c6 = get_credits('Fundamentals of Accounting',1,6,'BCA',1)

    m7 = get_marks('Programming In C - Lab',18,50,'BCA',1)
    g7 = grade_points_assigment(m7,50)
    c7 = get_credits('Programming In C - Lab',1,6,'BCA',1)

    m8 = get_marks('Computer Application - Lab',18,50,'BCA',1)
    g8 = grade_points_assigment(m8,50)
    c8 = get_credits('Computer Application - Lab',1,6,'BCA',1)

    total_marks_obtained = m1+m2+m3+m4+m5+m6+m7+m8
    total_marks = 700
    percentage = total_marks_obtained / total_marks * 100
    total_credits_obtained = c1+c2+c3+c4+c5+c6+c7+c8
    total_grade_points_obtained = g1+g2+g3+g4+g5+g6+g7+g8
    total_credit_points = (c1*g1) + (c2*g2) + (c3*g3) + (c4*g4) + (c5*g5) + (c6*g6) + (c7*g7) + (c8*g8)
    sgpa = total_credit_points / total_credits_obtained
    grade = Grades(percentage)
    final_output(total_marks_obtained,total_marks,percentage,total_grade_points_obtained,month,year,grade,sgpa)

def BCA_Sem_2():
    month = 'Sept'
    year = 2020
    m1 = get_marks('English',36,100,'BCA',2)
    g1 = grade_points_assigment(m1,100)
    c1 = get_credits('English',1,6,'BCA',2)

    m2 = get_marks('K/S/H',36,100,'BCA',2)
    g2 = grade_points_assigment(m2,100)
    c2 = get_credits('K/S/H',1,6,'BCA',2)

    m3 = get_marks('Data Structures using C',36,100,'BCA',2)
    g3 = grade_points_assigment(m3,100)
    c3 = get_credits('Data Structures using C',1,6,'BCA',2)

    m4 = get_marks('Object Oriented Programming using C++',36,100,'BCA',2)
    g4 = grade_points_assigment(m4,100)
    c4 = get_credits('Object Oriented Programming using C++',1,6,'BCA',2)

    m5 = get_marks('Operating System',36,100,'BCA',2)
    g5 = grade_points_assigment(m5,100)
    c5 = get_credits('Operating System',1,6,'BCA',2)

    m6 = get_marks('Numerical and Statistical Methods',36,100,'BCA',2)
    g6 = grade_points_assigment(m6,100)
    c6 = get_credits('Numerical and Statistical Methods',1,6,'BCA',2)

    m7 = get_marks('Data Structures Using C - Lab',18,50,'BCA',2)
    g7 = grade_points_assigment(m7,50)
    c7 = get_credits('Data Structures Using C - Lab',1,6,'BCA',2)

    m8 = get_marks('C++ - Lab',18,50,'BCA',2)
    g8 = grade_points_assigment(m8,50)
    c8 = get_credits('C++ - Lab',1,6,'BCA',2)

    m9 = get_marks('Indian Constitution and Human Rights',36,100,'BCA',2)
    g9 = grade_points_assigment(m9,100)
    c9 = get_credits('Indian Constitution and Human Rights',1,6,'BCA',2)
    
    total_marks_obtained = m1+m2+m3+m4+m5+m6+m7+m8+m9
    total_marks = 800
    percentage = total_marks_obtained / total_marks * 100
    total_marks_obtained = m1+m2+m3+m4+m5+m6+m7+m8+m9
    total_credits_obtained = c1+c2+c3+c4+c5+c6+c7+c8+c9
    total_grade_points_obtained = g1+g2+g3+g4+g5+g6+g7+g8+g9
    total_credit_points = (c1*g1) + (c2*g2) + (c3*g3) + (c4*g4) + (c5*g5) + (c6*g6) + (c7*g7) + (c8*g8) + (c9*g9)
    sgpa = total_credit_points / total_credits_obtained
    total_marks = 800
    percentage = total_marks_obtained / total_marks * 100
    grade = Grades(percentage)
    final_output(total_marks_obtained,total_marks,percentage,total_grade_points_obtained,month,year,grade,sgpa)

def BCA_Sem_3():
    month = 'Mar'
    year = 2021
    m1 = get_marks('English',35,100,'BCA',3)
    g1 = grade_points_assigment(m1,100)
    c1 = get_credits('English',1,6,'BCA',3)

    m2 = get_marks('K/S/H',35,100,'BCA',3)
    g2 = grade_points_assigment(m2,100)
    c2 = get_credits('K/S/H',1,6,'BCA',3)

    m3 = get_marks('Core Java',35,100,'BCA',3)
    g3 = grade_points_assigment(m3,100)
    c3 = get_credits('Core Java',1,6,'BCA',3)

    m4 = get_marks('Unix Operating System',35, 100,'BCA',3)
    g4 = grade_points_assigment(m4,100)
    c4 = get_credits('Unix Operating System',1,6,'BCA',3)

    m5 = get_marks('Database Management System',35,100,'BCA',3)
    g5 = grade_points_assigment(m5,100)
    c5 = get_credits('Database Management System',1,6,'BCA',3)

    m6 = get_marks('VB.Net Programming',35,100,'BCA',3)
    g6 = grade_points_assigment(m6,100)
    c6 = get_credits('VB.Net Programming',1,6,'BCA',3)

    m7 = get_marks('Core Java - Lab',18,50,'BCA',3)
    g7 = grade_points_assigment(m7,50)
    c7 = get_credits('Core Java - Lab',1,6,'BCA',3)

    m8 = get_marks('Unix - Lab',18,50,'BCA',3)
    g8 = grade_points_assigment(m8,50)
    c8 = get_credits('Unix - Lab',1,6,'BCA',3)

    m9 = get_marks('VB.Net and SQL - Lab',18,50,'BCA',3)
    g9 = grade_points_assigment(m9,50)
    c9 = get_credits('VB.Net and SQL - Lab',1,6,'BCA',3)

    m10 = get_marks('Human Resource Management',18,50,'BCA',3)
    g10 = grade_points_assigment(m10,50)
    c10 = get_credits('Human Resource Management',1,6,'BCA',3)

    m11 = get_marks('Open Elective: Electronics For ALl',18,50,'BCA',3)
    g11 = grade_points_assigment(m11,50)
    c11 = get_credits('Open Elective: Electronics For All',1,6,'BCA',3)

    total_marks_obtained = m1+m2+m3+m4+m5+m6+m7+m8+m9
    total_marks = 850
    percentage = total_marks_obtained / total_marks * 100
    total_credits_obtained = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11
    total_grade_points_obtained = g1+g2+g3+g4+g5+g6+g7+g8+g9+g10+g11
    total_credit_points = (c1*g1) + (c2*g2) + (c3*g3) + (c4*g4) + (c5*g5) + (c6*g6) + (c7*g7) + (c8*g8) + (c9*g9) + (c10*g10) + (c11*g11)
    sgpa = total_credit_points / total_credits_obtained
    grade = Grades(percentage)
    final_output(total_marks_obtained,total_marks,percentage,total_grade_points_obtained,month,year,grade,sgpa)

def BCA_Sem_4():
    month = 'Aug'
    year = 2021
    m1 = get_marks('English',35,100,'BCA',4)
    g1 = grade_points_assigment(m1,100)
    c1 = get_credits('English',1,6,'BCA',4)

    m2 = get_marks('K/S/H',35,100,'BCA',4)
    g2 = grade_points_assigment(m2,100)
    c2 = get_credits('K/S/H',1,6,'BCA',4)

    m3 = get_marks('Design And Analysis Of Algorithms',35,100,'BCA',4)
    g3 = grade_points_assigment(m3,100)
    c3 = get_credits('Design And Analysis Of Algorithms',1,6,'BCA',4)

    m4 = get_marks('Python',35,100,'BCA',4)
    g4 = grade_points_assigment(m4,100)
    c4 = get_credits('Python',1,6,'BCA',4)

    m5 = get_marks('Software Engineering',35,100,'BCA',4)
    g5 = grade_points_assigment(m5,100)
    c5 = get_credits('Software Engineering',1,6,'BCA',4)

    m6 = get_marks('Computer Graphics',35,100,'BCA',4)
    g6 = grade_points_assigment(m6,100)
    c6 = get_credits('Computer Graphics',1,6,'BCA',4)

    m7 = get_marks('Python - Lab',18,50,'BCA',4)
    g7 = grade_points_assigment(m7,50)
    c7 = get_credits('Python - Lab',1,6,'BCA',4)

    m8 = get_marks('Computer Graphics - Lab',18,50,'BCA',4)
    g8 = grade_points_assigment(m8,50)
    c8 = get_credits('Computer Graphics - Lab',1,6,'BCA',4)

    m9 = get_marks('Mini Project',18,50,'BCA',4)
    g9 = grade_points_assigment(m9,50)
    c9 = get_credits('Mini Project',1,6,'BCA',4)

    m10 = get_marks('Value Education',18,50,'BCA',4)
    g10 = grade_points_assigment(m10,50)
    c10 = get_credits('Value Education',1,6,'BCA',4)

    g11 = 1
    c11 = get_credits('Skill Development',1,6,'BCA',4)

    total_marks_obtained = m1+m2+m3+m4+m5+m6+m7+m8+m9+m10
    total_marks = 800
    percentage = total_marks_obtained / total_marks * 100
    total_credits_obtained = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11
    total_grade_points_obtained = g1+g2+g3+g4+g5+g6+g7+g8+g9+g10+g11
    total_credit_points = (c1*g1) + (c2*g2) + (c3*g3) + (c4*g4) + (c5*g5) + (c6*g6) + (c7*g7) + (c8*g8) + (c9*g9) + (c10*g10) + (c11 * g11)
    sgpa = total_credit_points / total_credits_obtained
    grade = Grades(percentage)
    final_output(total_marks_obtained,total_marks,percentage,total_grade_points_obtained,month,year,grade,sgpa)

def BCA_Sem_5():
    month = 'Mar'
    year = 2022
    m1 = get_marks('Internet Technologies',35,100,'BCA',5)
    g1 = grade_points_assigment(m1,100)
    c1 = get_credits('Internet Technologies',35,100,'BCA',5)

    m2 = get_marks('Artificial Intelligence',35,100,'BCA',5)
    g2 = grade_points_assigment(m2,100)
    c2 = get_credits('Internet Technologies',35,100,'BCA',5)

    m3 = get_marks('Computer Networks',35,100,'BCA',5)
    g3 = grade_points_assigment(m3,100)
    c3 = get_credits('Internet Technologies',35,100,'BCA',5)

    m4 = get_marks('Web Application Development',35,100,'BCA',5)
    g4 = grade_points_assigment(m4,100)
    c4 = get_credits('Internet Technologies',35,100,'BCA',5)

    m5 = get_marks('Cloud Computing',35,100,'BCA',5)
    g5 = grade_points_assigment(m5,100)
    c5 = get_credits('Cloud Computing',35,100,'BCA',5)

    m6 = get_marks('Internet Technologies - Lab',18,50,'BCA',5)
    g6 = grade_points_assigment(m6,50)
    c6 = get_credits('Internet Technologies - Lab',35,50,'BCA',5)

    m7 = get_marks('Web Application Development - Lab',18,50,'BCA',5)
    g7 = grade_points_assigment(m7,50)
    c7 = get_credits('Web Application Development - Lab',35,50,'BCA',5)

    m8 = get_marks('Simulation Project - Lab',18,50,'BCA',5)
    g8 = grade_points_assigment(m8,50)
    c8 = get_credits('Simulation Project - Lab',35,50,'BCA',5)

    m9 = get_marks('Communicative English',18,50,'BCA',5)
    g9 = grade_points_assigment(m9,50)
    c9 = get_credits('Communicative English',35,50,'BCA',5)

    total_marks_obtained = m1+m2+m3+m4+m5+m6+m7+m8+m9
    total_marks = 800
    percentage = total_marks_obtained / total_marks * 100
    total_credits_obtained = c1+c2+c3+c4+c5+c6+c7+c8+c9
    total_grade_points_obtained = g1+g2+g3+g4+g5+g6+g7+g8+g9
    total_credit_points = (c1*g1) + (c2*g2) + (c3*g3) + (c4*g4) + (c5*g5) + (c6*g6) + (c7*g7) + (c8*g8) + (c9*g9)
    sgpa = total_credit_points / total_credits_obtained
    grade = Grades(percentage)
    final_output(total_marks_obtained,total_marks,percentage,total_grade_points_obtained,month,year,grade,sgpa)

def BCA_Sem_6():
    print('Not Available')
    keypress()
course_menu()