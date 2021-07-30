import sys

roll_number = []
student_name = []
student_section = []
course_1 = []
course1_MA1 = []
course1_MA2 = []
course1_MA3 = []
course1_MA4 = []
course1_MA5 = []
course_2 = []
course2_MA1 = []
course2_MA2 = []
course2_MA3 = []
course2_MA4 = []
course2_MA5 = []
course_3 = []
course3_MA1 = []
course3_MA2 = []
course3_MA3 = []
course3_MA4 = []
course3_MA5 = []
course_4 = []
course4_MA1 = []
course4_MA2 = []
course4_MA3 = []
course4_MA4 = []
course4_MA5 = []

class student_info:
    
    #add student information 
    def addition_studinfo(self):
        print('To add student information-')
        stud_roll_no = int(input('Enter Roll Number:'))
        roll_number.append(stud_roll_no)
        
        stud_name = input('Enter Student Name:')
        student_name.append(stud_name)
        
        stud_sec = input('Enter Student Section:')
        student_section.append(stud_sec)
        
        course_name = input('Enter name of course 1:')
        course_1.append(course_name)
        
        c1_MA1 = int(input('Enter marks of Mandatory Assignment 1:'))
        course1_MA1.append(c1_MA1)
        if c1_MA1 >= 9:
            print ('Pass')
        else:
            print ('Fail')

        c1_MA2 = int(input('Enter marks of Mandatory Assignment 2:'))
        course1_MA2.append(c1_MA2)
        if c1_MA2 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        c1_MA3 = int(input('Enter marks of Mandatory Assignment 3:'))
        course1_MA3.append(c1_MA3)
        if c1_MA3 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        print ('Enter marks of Mandatory Assignment 4:', end=" ")
        c1_MA4 = int(input('Enter marks of Mandatory Assignment 4:'))
        course1_MA4.append(c1_MA4)
        if c1_MA4 >= 9:
            print ('Pass')
        else:
            print ('Fail')

        c1_MA5 = int(input('Enter marks of Mandatory Assignment 5:'))
        course1_MA5.append(c1_MA5)
        if c1_MA5 >= 9:
            print ('Pass')
        else:
            print ('Fail')
            
        #course 2 
        print ('Enter name of course 2:', end=" ")
        course_name = input()
        course_2.append(course_name)
        
        c2_MA1 = int(input('Enter marks of Mandatory Assignment 1:'))
        course2_MA1.append(c2_MA1)
        if c2_MA1 >= 9:
            print ('Pass')
        else:
            print ('Fail')

        c2_MA2 = int(input('Enter marks of Mandatory Assignment 2:'))
        course2_MA2.append(c2_MA2)
        if c2_MA2 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        c2_MA3 = int(input('Enter marks of Mandatory Assignment 3:'))
        course1_MA3.append(c2_MA3)
        if c2_MA3 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        c2_MA4 = int(input('Enter marks of Mandatory Assignment 4:'))
        course1_MA4.append(c2_MA4)
        if c2_MA4 >= 9:
            print ('Pass')
        else:
            print ('Fail')

        c2_MA5 = int(input('Enter marks of Mandatory Assignment 5:'))
        course1_MA5.append(c2_MA5)
        if c2_MA5 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        #course 3 
        course_name = input('Enter name of course 3:')
        course_3.append(course_name)

        c3_MA1 = int(input('Enter marks of Mandatory Assignment 1:'))
        course3_MA1.append(c3_MA1)
        if c3_MA1 >= 9:
            print ('Pass')
        else:
            print ('Fail')

        c3_MA2 = int(input('Enter marks of Mandatory Assignment 2:'))
        course3_MA2.append(c3_MA2)
        if c3_MA2 >= 9:
            print ('Pass')
        else:
            print ('Fail')

        c3_MA3 = int(input('Enter marks of Mandatory Assignment 3:'))
        course3_MA3.append(c3_MA3)
        if c3_MA3 >= 9:
            print ('Pass')
        else:
            print ('Fail')

        c3_MA4 = int(input('Enter marks of Mandatory Assignment 4:'))
        course3_MA4.append(c3_MA4)
        if c3_MA4 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        

        c3_MA5 = int(input('Enter marks of Mandatory Assignment 5:'))
        course3_MA5.append(c3_MA5)
        if c3_MA5 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        #course 4 
        course_name = input('Enter name of course 4 :')
        course_4.append(course_name)

        c4_MA1 = int(input('Enter marks of Mandatory Assignment 1:'))
        course4_MA1.append(c4_MA1)
        if c4_MA1 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        c4_MA2 = int(input('Enter marks of Mandatory Assignment 2:'))
        course4_MA2.append(c4_MA2)
        if c4_MA2 >= 9:
            print ('Pass')
        else:
            print ('Fail')

        c4_MA3 = int(input('Enter marks of Mandatory Assignment 3:'))
        course4_MA3.append(c4_MA3)
        if c4_MA3 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        c4_MA4 = int(input('Enter marks of Mandatory Assignment 4:'))
        course4_MA4.append(c4_MA4)
        if c4_MA4 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        c4_MA5 = int(input('Enter marks of Mandatory Assignment 5:'))
        course4_MA5.append(c4_MA5)
        if c4_MA5 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
    #remove a student information 
    def remove_studinfo(self):
        roll_no = int(input('Enter the roll number of student:'))
        stud_index = roll_number.index(roll_no)
          
        roll_number.remove(roll_no[stud_index])
        student_name.remove(student_name[stud_index])
        student_section.remove(student_section[stud_index])
        course_1.remove(course_1[stud_index])
        course1_MA1.remove(course1_MA1[stud_index])
        course1_MA2.remove(course1_MA2[stud_index])
        course1_MA3.remove(course1_MA3[stud_index])  
        course1_MA4.remove(course1_MA4[stud_index])
        course1_MA5.remove(course1_MA5[stud_index])  
        course_2.remove(course_2[stud_index])
        course2_MA1.remove(course2_MA1[stud_index])
        course2_MA2.remove(course2_MA2[stud_index])
        course2_MA3.remove(course2_MA3[stud_index])  
        course2_MA4.remove(course2_MA4[stud_index])
        course2_MA5.remove(course2_MA5[stud_index])  
        course_3.remove(course_3[stud_index])
        course3_MA1.remove(course3_MA1[stud_index])
        course3_MA2.remove(course3_MA2[stud_index])
        course3_MA3.remove(course3_MA3[stud_index])  
        course3_MA4.remove(course3_MA4[stud_index])
        course3_MA5.remove(course3_MA5[stud_index]) 
        course_4.remove(course_4[stud_index])
        course4_MA1.remove(course4_MA1[stud_index])
        course4_MA2.remove(course4_MA2[stud_index])
        course4_MA3.remove(course4_MA3[stud_index])  
        course4_MA4.remove(course4_MA4[stud_index])
        course4_MA5.remove(course4_MA5[stud_index])  
          
        print ('\nDone!\n')
          
    #Modifying a particular student information
    def modify_studinfo(self):
        print ('Choose from: Roll Number, Student Name, Section, Course 1, C1MA1, C1MA2, C1MA3, C1MA4, C1MA5, Course 2, C2MA1, C2MA2, C2MA3, C2MA4, C2MA5, Course 3, C3MA1, C3MA2, C3MA3, C3MA4, C3MA5, Course 4, C4MA1, C4MA2, C4MA3, C4MA4, C4MA5')
        field = input('What field do you want to modify?')
          
        if field == 'roll number':
            rollno_replace = int(input("Enter student's old roll number:"))
            rollno_index = roll_number.index(rollno_replace)

            new_rollno = input('Enter new roll number: ')
            roll_number[rollno_index] = new_rollno  
            print ('Updated!\n')  
             
        elif field == 'student name':
            name_replace = input("Enter student's old name:")
            name_index = student_name.index(name_replace)
             
            new_name = input('Enter new student name: ')
            student_name[name_index] = new_name  
            print ('Updated!\n')
         
        elif field == 'section':
            section_replace = input("Enter student's old section:")
            section_index = student_section.index(section_replace)
             
            new_section = input('Enter new section: ')
            student_section[section_index] = new_section
            print ('Updated!\n') 
            
        elif field == 'course 1':
            course1_replace = input("Enter student's old course 1 :")
            course1_index = course_1.index(course1_replace)
             
            new_course1 = input('Enter new course 1 : ')
            course_1[course1_index] = new_course1
            print ('Updated!\n')
             
        elif field == 'C1MA1':
            C1MA1_replace = int(input("Enter student's old marks for mandatory assignment 1:"))
            C1MA1_index = course1_MA1.index(C1MA1_replace)
             
            new_C1MA1 = input('Enter new marks for mandatory assignment 1: ')
            course1_MA1[C1MA1_index] = new_C1MA1
            print ('Updated!\n')
             
        elif field == 'C1MA2':
            C1MA2_replace = int(input("Enter student's old marks for mandatory assignment 2:"))
            C1MA2_index = course1_MA2.index(C1MA2_replace)
            new_C1MA2 = input('Enter new marks for mandatory assignment 2: ')
            course1_MA2[C1MA2_index] = new_C1MA2
            print ('Updated!\n')
            
        elif field == 'C1MA3':
            C1MA3_replace = int(input("Enter student's old marks for mandatory assignment 3:"))
            C1MA3_index = course1_MA3.index(C1MA3_replace)
             
            new_C1MA3 = input('Enter new marks for mandatory assignment 3: ')
            course1_MA3[C1MA3_index] = new_C1MA3
            print ('Updated!\n')
             
        elif field == 'C1MA4':
            C1MA4_replace = int(input("Enter student's old marks for mandatory assignment 4:"))
            C1MA4_index = course1_MA4.index(C1MA4_replace)
             
            new_C1MA4 = input('Enter new marks for mandatory assignment 4: ')
            course1_MA4[C1MA4_index] = new_C1MA4
            print ('Updated!\n')
             
        elif field == 'C1MA5':
            C1MA5_replace = int(input("Enter student's old marks for mandatory assignment 5:"))
            C1MA5_index = course1_MA5.index(C1MA5_replace)
             
            new_C1MA5 = input('Enter new marks for mandatory assignment 5: ')
            course1_MA5[C1MA5_index] = new_C1MA5
            print ('Updated!\n')
             
        elif field == 'course 2':
            course2_replace = input("Enter student's old course 2 :")
            course2_index = course_2.index(course2_replace)
             
            new_course2 = input('Enter new course 2 : ')
            course_2[course2_index] = new_course2
            print ('Updated!\n')
             
        elif field == 'C2MA1':
            C2MA1_replace = int(input("Enter student's old marks for mandatory assignment 1:"))
            C2MA1_index = course2_MA1.index(C2MA1_replace)
             
            new_C2MA1 = input('Enter new marks for mandatory assignment 1: ')
            course2_MA1[C2MA1_index] = new_C2MA1
            print ('Updated!\n')
             
        elif field == 'C2MA2':
            C2MA2_replace = int(input("Enter student's old marks for mandatory assignment 2:"))
            C2MA2_index = course2_MA2.index(C2MA2_replace)
            new_C2MA2 = input('Enter new marks for mandatory assignment 2: ')
            course2_MA2[C2MA2_index] = new_C2MA2
            print ('Updated!\n')
             
        elif field == 'C2MA3':
            C2MA3_replace = int(input("Enter student's old marks for mandatory assignment 3:"))
            C2MA3_index = course2_MA3.index(C2MA3_replace)
             
            new_C2MA3 = input('Enter new marks for mandatory assignment 3: ')
            course2_MA3[C2MA3_index] = new_C2MA3
            print ('Updated!\n')
             
        elif field == 'C2MA4':
            C2MA4_replace = int(input("Enter student's old marks for mandatory assignment 4:"))
            C2MA4_index = course2_MA4.index(C2MA4_replace)
             
            new_C2MA4 = input('Enter new marks for mandatory assignment 4: ')
            course2_MA4[C2MA4_index] = new_C2MA4
            print ('Updated!\n')
             
        elif field == 'C2MA5':
            C2MA5_replace = int(input("Enter student's old marks for mandatory assignment 5:"))
            C2MA5_index = course2_MA5.index(C2MA5_replace)
             
            new_C2MA5 = input('Enter new marks for mandatory assignment 5: ')
            course2_MA5[C2MA5_index] = new_C2MA5
            print ('Updated!\n')
             
        elif field == 'course 3':
            course3_replace = input("Enter student's old course 3 :")
            course3_index = course_3.index(course3_replace)
             
            new_course3 = input('Enter new course 3 : ')
            course_3[course3_index] = new_course3
            print ('Updated!\n')
             
        elif field == 'C3MA1':
            C3MA1_replace = int(input("Enter student's old marks for mandatory assignment 1:"))
            C3MA1_index = course3_MA1.index(C3MA1_replace)
             
            new_C3MA1 = input('Enter new marks for mandatory assignment 1: ')
            course3_MA1[C3MA1_index] = new_C3MA1
            print ('Updated!\n')
             
        elif field == 'C3MA2':
            C3MA2_replace = int(input("Enter student's old marks for mandatory assignment 2:"))
            C3MA2_index = course3_MA2.index(C3MA2_replace)
            new_C3MA2 = input('Enter new marks for mandatory assignment 2: ')
            course3_MA2[C3MA2_index] = new_C3MA2
            print ('Updated!\n')
             
        elif field == 'C3MA3':
            C3MA3_replace = int(input("Enter student's old marks for mandatory assignment 3:"))
            C3MA3_index = course3_MA3.index(C3MA3_replace)
             
            new_C3MA3 = input('Enter new marks for mandatory assignment 3: ')
            course3_MA3[C3MA3_index] = new_C3MA3
            print ('Updated!\n')
             
        elif field == 'C3MA4':
            C3MA4_replace = int(input("Enter student's old marks for mandatory assignment 4:"))
            C3MA4_index = course3_MA4.index(C3MA4_replace)
             
            new_C3MA4 = input('Enter new marks for mandatory assignment 4: ')
            course3_MA4[C3MA4_index] = new_C3MA4
            print ('Updated!\n')
             
        elif field == 'C3MA5':
            C3MA5_replace = int(input("Enter student's old marks for mandatory assignment 5:"))
            C3MA5_index = course3_MA5.index(C3MA5_replace)
             
            new_C3MA5 = input('Enter new marks for mandatory assignment 5: ')
            course3_MA5[C3MA5_index] = new_C3MA5
            print ('Updated!\n')
             
        elif field == 'course 4':
            course4_replace = input("Enter student's old course 4 :")
            course4_index = course_4.index(course4_replace)
             
            new_course4 = input('Enter new course 1 : ')
            course_4[course4_index] = new_course4
            print ('Updated!\n')
             
        elif field == 'C4MA1':
            C4MA1_replace = int(input("Enter student's old marks for mandatory assignment 1:"))
            C4MA1_index = course4_MA1.index(C4MA1_replace)
             
            new_C4MA1 = input('Enter new marks for mandatory assignment 1: ')
            course4_MA1[C4MA1_index] = new_C4MA1
            print ('Updated!\n')
             
        elif field == 'C4MA2':
            C4MA2_replace = int(input("Enter student's old marks for mandatory assignment 2:"))
            C4MA2_index = course4_MA2.index(C4MA2_replace)
            new_C4MA2 = input('Enter new marks for mandatory assignment 2: ')
            course4_MA2[C4MA2_index] = new_C4MA2
            print ('Updated!\n')
             
        elif field == 'C4MA3':
            C4MA3_replace = int(input("Enter student's old marks for mandatory assignment 3:"))
            C4MA3_index = course4_MA3.index(C4MA3_replace)
             
            new_C4MA3 = input('Enter new marks for mandatory assignment 3: ')
            course4_MA3[C4MA3_index] = new_C4MA3
            print ('Updated!\n')
             
        elif field == 'C4MA4':
            C4MA4_replace = int(input("Enter student's old marks for mandatory assignment 4:"))
            C4MA4_index = course4_MA4.index(C4MA4_replace)
             
            new_C4MA4 = input('Enter new marks for mandatory assignment 4: ')
            course4_MA4[C4MA4_index] = new_C4MA4
            print ('Updated!\n')
             
        elif field == 'C4MA5':
            C4MA5_replace = int(input("Enter student's old marks for mandatory assignment 5:"))
            C4MA5_index = course4_MA5.index(C4MA5_replace)
             
            new_C4MA5 = input('Enter new marks for mandatory assignment 5: ')
            course4_MA5[C4MA5_index] = new_C4MA5
            print ('Updated!\n') 
             
    #Retrieve entire students list
    def retrieve_studinfo(self):
        print("Student's Roll Number: ", end = "/n")
        for roll_num in roll_number:
            print(roll_num)
          
        print("Student's Name : ", end="\n")

        for name in student_name:
            print(name+'\n')
        print("Student's Sections :", end="\n")

        for section in student_section:
            print(section+'\n')
        print("Course 1 taken by each student :", end="\n")

        for course in course_1:
            print(course+'\n')
        print("Marks obtained by each student in course 1 mandatory assignment 1 :", end="\n")
          
        for c1ma1 in course1_MA1:
            if c1ma1 >= 9:
                print(c1ma1, 'pass\n')
            else:
                print (c1ma1, 'fail\n')
        print("Marks obtained by each student in course 1 mandatory assignment 2 :", end="\n")

        for c1ma2 in course1_MA2:
            if c1ma2 >= 9:
                print(c1ma2, 'pass\n')
            else:
                print (c1ma2, 'fail\n')
        print("Marks obtained by each student in course 1 mandatory assignment 3 :\n")

        for c1ma3 in course1_MA3:
            if c1ma3 >= 9:
                print(c1ma3, 'pass\n')
            else:
                print (c1ma3, 'fail\n')
        print("Marks obtained by each student in course 1 mandatory assignment 4 :\n")

        for c1ma4 in course1_MA4:
            if c1ma4 >= 9:
                print(c1ma4, 'pass\n')
            else:
                print (c1ma4, 'fail\n')
        print("Marks obtained by each student in course 1 mandatory assignment 5 :\n")

        for c1ma5 in course1_MA5:
            if c1ma5 >= 9:
                print(c1ma5, 'pass\n')
            else:
                print (c1ma5, 'fail\n')
        print("Course 2 taken by each student :\n")

        for course in course_2:
            print(course+'\n')
        print("Marks obtained by each student in course 1 mandatory assignment 3 :\n")

        for c2ma1 in course2_MA1:
            if c2ma1 >= 9:
                print(c2ma1, 'pass\n')
            else:
                print (c2ma1, 'fail\n')
        print("Marks obtained by each student in course 1 mandatory assignment 4 :\n")

        for c2ma2 in course1_MA4:
            if c2ma2 >= 9:
                print(c2ma2, 'pass\n')
            else:
                print (c2ma2, 'fail\n')
        print("Marks obtained by each student in course 1 mandatory assignment 5 :\n")

        for c2ma3 in course1_MA5:
            if c2ma3 >= 9:
                print(c2ma3, 'pass\n')
            else:
                print (c2ma3, 'fail\n')
          
        for c2ma4 in course1_MA5:
            if c2ma4 >= 9:
                print(c2ma4, 'pass\n')
            else:
                print (c2ma4, 'fail\n')

        for c2ma5 in course1_MA5:
             if c2ma5 >= 9:
                print(c2ma5, 'pass\n')
             else:
                print (c2ma5, 'fail\n')
          
        for course in course_3:
              print(course+'\n')
        print("Marks obtained by each student in course 3 mandatory assignment 3 :\n")

        for c3ma1 in course3_MA1:
            if c3ma1 >= 9:
                print(c3ma1, 'pass\n')
            else:
                print (c3ma1, 'fail\n')

        print("Marks obtained by each student in course 3 mandatory assignment 4 :\n")

        for c3ma2 in course1_MA4:
            if c3ma2 >= 9:
                print(c3ma2, 'pass\n')
            else:
                print (c3ma2, 'fail\n')
          
        print("Marks obtained by each student in course 3 mandatory assignment 5 :\n")

        for c3ma3 in course3_MA5:
            if c3ma3 >= 9:
                print(c3ma3, 'pass\n')
            else:
                print (c3ma3, 'fail\n')
          
        for c3ma4 in course1_MA5:
            if c2ma4 >= 9:
                 print(c2ma4, 'pass\n')
            else:
                 print (c2ma4, 'fail\n')
          
        for c3ma5 in course3_MA5:
            if c3ma5 >= 9:
                print(c3ma5, 'pass\n')
            else:
                print (c3ma5, 'fail\n')
          
        for course in course_4:
            print(course+'\n')
        print("Marks obtained by each student in course 4 mandatory assignment 3 :\n")

        for c4ma1 in course4_MA1:
            if c4ma1 >= 9:
                print(c4ma1, 'pass\n')
            else:
                print (c4ma1, 'fail\n')
        print("Marks obtained by each student in course 4 mandatory assignment 4 :\n")

        for c4ma2 in course4_MA4:
            if c4ma2 >= 9:
                print(c4ma2, 'pass\n')
            else:
                print (c4ma2, 'fail\n')
        print("Marks obtained by each student in course 4 mandatory assignment 5 :\n")

        for c4ma3 in course3_MA5:
            if c4ma3 >= 9:
                print(c4ma3, 'pass\n')
            else:
                print (c4ma3, 'fail\n')
          
        for c4ma4 in course1_MA5:
            if c4ma4 >= 9:
                print(c4ma4, 'pass\n')
            else:
                print (c4ma4, 'fail\n')
          
        for c4ma5 in course3_MA5:
            if c4ma5 >= 9:
                print(c4ma5, 'pass\n')
            else:
                print (c4ma5, 'fail\n')
          
stud = student_info()

if __name__ == '__main__':

    print ('\nHelp Desk')
    print ('How can we help you?') 
    
    while True:
        list_print=['1.Add student information','2.Delete particular student information','3.Modify particular student information','4.Retrieve entire student information','5.Exit the program']
        for i in list_print:
            print(i)
        
        select_option = int (input("Choose the option for execution:\n"))
        
        if select_option == 1:
            stud.addition_studinfo()
        elif select_option == 2:
            stud.remove_studinfo()
        elif select_option == 3:
            stud.modify_studinfo()
        elif select_option == 4:
            stud.retrieve_studinfo()
        elif select_option == 5:
            print ('Have a nice day!')
sys.exit()
