import sys 

roll_number = []
student_name = []
course3_MA1 = []
course3_MA2 = []
course3_MA3 = []
course3_MA4 = []
course3_MA5 = []

class visual_analytics():
    
    def add_stud_c3(self):

        stud_roll_no = int(input('Enter Roll Number:'))
        roll_number.append(stud_roll_no)
        
        stud_name = input('Enter Student Name:')
        student_name.append(stud_name)
        
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
        
        print ('Enter marks of Mandatory Assignment 3:', end=" ")
        c3_MA3 = int(input())
        course3_MA3.append(c3_MA3)
        if c3_MA3 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        print ('Enter marks of Mandatory Assignment 4:', end=" ")
        c3_MA4 = int(input())
        course3_MA4.append(c3_MA4)
        if c3_MA4 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        print ('Enter marks of Mandatory Assignment 5:', end=" ")
        c3_MA5 = int(input())
        course3_MA5.append(c3_MA5)
        if c3_MA5 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
    def remove_stud_c1(self):

        roll_no = int(input('Enter the roll number of student:'))
        stud_index = roll_number.index(roll_no)
          
        roll_number.remove(roll_no[stud_index])
        student_name.remove(student_name[stud_index])
        course3_MA1.remove(course3_MA1[stud_index])
        course3_MA2.remove(course3_MA2[stud_index])
        course3_MA3.remove(course3_MA3[stud_index])  
        course3_MA4.remove(course3_MA4[stud_index])
        course3_MA5.remove(course3_MA5[stud_index])
    
    def student_pass(self):
        count1 = 0 
        for a in course3_MA1: 
            if course3_MA1 >= 9: 
                count1 = count1 + 1 
            print ('Number of students passing the assignment 1:', count1)
        
        count2= 0
        for b in course3_MA2: 
            if course3_MA2 >= 9: 
                count2 = count2 + 1 
            print ('Number of students passing the assignment 2:', count2)
        
        count3 = 0
        for c in course3_MA3: 
            if course3_MA3 >= 9: 
                count3 = count3 + 1 
            print ('Number of students passing the assignment 3:', count3)
        
        count4 = 0
        for d in course3_MA4: 
            if course3_MA4 >= 9: 
                count4 = count4 + 1 
            print ('Number of students passing the assignment 4:', count4)

        count5 = 0
        for e in course3_MA5: 
            if course3_MA5 >= 9: 
                count5 = count5 + 1 
            print ('Number of students passing the assignment 5:', count5)

    def student_fail(self):
        co1 = 0 
        for v in course3_MA1: 
            if course3_MA1 < 9: 
                co1 = co1 + 1 
            print ('Number of students who failed the assignment 1:', co1)
        
        co2= 0
        for w in course3_MA2: 
            if course3_MA2 < 9: 
                co2 = co2 + 1 
            print ('Number of students who failed the assignment 2:', co2)
        
        co3 = 0
        for x in course3_MA3: 
            if course3_MA3 >= 9: 
                co3 = co3 + 1 
            print ('Number of students who failed the assignment 3:', co3)
        
        co4 = 0
        for y in course3_MA4: 
            if course3_MA4 >= 9: 
                co4 = co4 + 1 
            print ('Number of students who failed the assignment 4:', co4)

        co5 = 0
        for pass_ in course3_MA5: 
            if course3_MA5 >= 9: 
                co5 = co5 + 1 
            print ('Number of students who failed the assignment 5:', co5)

visual = visual_analytics()

if __name__ == '__main__':
    
    print ('\nHelp Desk')
    print ('How can we help you?') 
    
    while True:
        list_print = ['1.Add student information','2.Delete particular student information','3.Number of students who passed','4.Number of students who failed','5.Exit the program']
        for i in list_print:
            print(i)
        select_option = int (input("Choose the option for execution:"))
        print('\n')
        
        if select_option == 1:
            visual.add_stud_c3()
        elif select_option == 2:
            visual.remove_stud_c3()
        elif select_option == 3:
            visual.student_pass()
        elif select_option == 4:
            visual.student_fail()
        elif select_option == 5:
            print ('Have a nice day!')
sys.exit()
