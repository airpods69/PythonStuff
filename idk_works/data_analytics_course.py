import sys 

roll_number =[]
student_name =[]
course2_MA1 =[]
course2_MA2 =[]
course2_MA3 =[]
course2_MA4 =[]
course2_MA5 =[]

class data_analytics():
    
    def add_stud_c2(self):
       
        print('Enter Roll Number:', end=" ")
        stud_roll_no = int(input())
        roll_number.append(stud_roll_no)
        
        print ('Enter Student Name:', end=" ")
        stud_name = input()
        student_name.append(stud_name)
        
        print ('Enter marks of Mandatory Assignment 1:', end=" ")
        c2_MA1 = int(input())
        course2_MA1.append(c2_MA1)
        if c2_MA1 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        print ('Enter marks of Mandatory Assignment 2:', end=" ")
        c2_MA2 = int(input())
        course2_MA2.append(c2_MA2)
        if c2_MA2 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        print ('Enter marks of Mandatory Assignment 3:', end=" ")
        c2_MA3 = int(input())
        course2_MA3.append(c2_MA3)
        if c2_MA3 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        print ('Enter marks of Mandatory Assignment 4:', end=" ")
        c2_MA4 = int(input())
        course2_MA4.append(c2_MA4)
        if c2_MA4 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
        print ('Enter marks of Mandatory Assignment 5:', end=" ")
        c2_MA5 = int(input())
        course2_MA5.append(c2_MA5)
        if c2_MA5 >= 9:
            print ('Pass')
        else:
            print ('Fail')
        
    def remove_stud_c2(self):
        
        print('Enter the roll number of student:')
        roll_no = int(input())
        stud_index = roll_number.index(roll_no)
          
        roll_number.remove(roll_no[stud_index])
        student_name.remove(student_name[stud_index])
        course2_MA1.remove(course2_MA1[stud_index])
        course2_MA2.remove(course2_MA2[stud_index])
        course2_MA3.remove(course2_MA3[stud_index])  
        course2_MA4.remove(course2_MA4[stud_index])
        course2_MA5.remove(course2_MA5[stud_index])
    
    def student_pass(self):
        count1 = 0 
        for a in course2_MA1: 
            if course2_MA1 >= 9: 
                count1 = count1 + 1 
            print ('Number of students passing the assignment 1:', count1)
        
        count2= 0
        for b in course2_MA2: 
            if course2_MA2 >= 9: 
                count2 = count2 + 1 
            print ('Number of students passing the assignment 2:', count2)
        
        count3 = 0
        for c in course2_MA3: 
            if course2_MA3 >= 9: 
                count3 = count3 + 1 
            print ('Number of students passing the assignment 3:', count3)
        
        count4 = 0
        for d in course2_MA4: 
            if course2_MA4 >= 9: 
                count4 = count4 + 1 
            print ('Number of students passing the assignment 4:', count4)

        count5 = 0
        for e in course2_MA5: 
            if course2_MA5 >= 9: 
                count5 = count5 + 1 
            print ('Number of students passing the assignment 5:', count5)

    def student_fail(self):
        co1 = 0 
        for v in course2_MA1: 
            if course2_MA1 < 9: 
                co1 = co1 + 1 
            print ('Number of students who failed the assignment 1:', co1)
        
        co2= 0
        for w in course2_MA2: 
            if course2_MA2 < 9: 
                co2 = co2 + 1 
            print ('Number of students who failed the assignment 2:', co2)
        
        co3 = 0
        for x in course2_MA3: 
            if course2_MA3 >= 9: 
                co3 = co3 + 1 
            print ('Number of students who failed the assignment 3:', co3)
        
        co4 = 0
        for y in course2_MA4: 
            if course2_MA4 >= 9: 
                co4 = co4 + 1 
            print ('Number of students who failed the assignment 4:', co4)

        co5 = 0
        for pass_ in course2_MA5: 
            if course2_MA5 >= 9: 
                co5 = co5 + 1 
            print ('Number of students who failed the assignment 5:', co5)

data = data_analytics()

if __name__ == '__main__':
    print ('\n')
    
    print ('Help Desk')
    print ('How can we help you?')
    
    run = True 
    
    while run:
        print ('1.Add student information')
        print ('2.Delete particular student information')
        print ('3.Number of students who passed')
        print ('4.Number of students who failed')
        print ('5.Exit the program')
       
        select_option = int (input("Choose the option for execution:"))
        print('\n')
        
        if select_option == 1:
            data.add_stud_c2()
        elif select_option == 2:
            data.remove_stud_c2()
        elif select_option == 3:
            data.student_pass()
        elif select_option == 4:
            data.student_fail()
        elif select_option == 5:
            print ('Have a nice day!')
sys.exit()