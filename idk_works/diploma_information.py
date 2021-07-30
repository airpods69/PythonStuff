import sys 
course_1 = []
course_2 = []
course_3 = []
course_4 = []
student_pass = []
student_fail = []
student_distinction = []

class diploma_information:
    
    #Add course
    def add_course(self):
        print('Add courses - \n')
        print('Course 1:', end=" ")
        course1 = input()
        course_1.append(course1)
        
        print('Course 2:', end=" ")
        course2 = input()
        course_2.append(course2)
        
        print('Course 3:', end=" ")
        course3 = input()
        course_3.append(course3)
        
        print('Course 4:', end=" ")
        course4 = input()
        course_4.append(course4)
        
        print ('\nDone!\n')
        
    # to remove course    
    def remove_course(self):
        list_print=['Course to be deleted','1. Python Programming','2. Data Analytics and Machine Learning','3. Visual Analytics','4. Text Analytics']
        for i in list_print:
            print(i)
        
        course_remove = input()
        
        if course_remove == 1:
            course_1.remove()
        elif course_remove == 2:
            course_2.remove()
        elif course_remove == 3:
            course_3.remove() 
        elif course_remove == 4:
            course_4.remove()
            
        print ('\nDone!\n')
            
    #add students who have passed    
    def stud_pass(self):
        stud_pass_name = input ('Enter student name - ')
        student_pass.append(stud_pass_name)
        
        print ('\nDone!\n')
    
    #add students who have failed
    def stud_fail(self):
        stud_fail_name = input ('Enter student name - ')
        student_fail.append(stud_fail_name)
        
        print ('\nDone!\n')
     
    #add students who have passed with distinction
    def stud_dist(self):
        stud_dist_name = input ('Enter student name - ')
        student_distinction.append(stud_dist_name)
        
        print ('\nDone!\n')
        
    #retrieve information of the course
    def retrieve_course_info(self):
        
        print ('List of Students who have passed: ')
        for pass_stud in student_pass:
            print (pass_stud+'\n')
            
        print ('List of Students who have failed: ')
        for fail_stud in student_fail:
            print (fail_stud+'\n')
            
        print ('List of Students who have passed with distinction: ')
        for dist_stud in student_distinction :
            print (dist_stud+'\n')

dip = diploma_information()

if __name__ == '__main__':
    
    print ('\nHelp Desk')
    print ('How can we help you?')
    
    while True:
        list_print=['1.Add course','2.Delete course','3.List student who passed','4.list student who failed','5.List student who passed with distinction','6.Retrieve course information']
        for i in list_print:
            print(i)
        
        select_option = int (input("Choose the option :"))
        print('\n')
        
        if select_option == 1:
            dip.add_course()
        elif select_option == 2:
            dip.remove_course()
        elif select_option == 3:
            dip.stud_pass()
        elif select_option == 4:
            dip.stud_fail()
        elif select_option == 5:
            dip.stud_dist()
        elif select_option == 6:
            dip.retrieve_course_info()
sys.exit()
