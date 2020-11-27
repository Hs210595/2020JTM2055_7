class lab:

    def __init__(self,name,email,role):
        self.name=name
        self.email=email
        self.role=role

    def gettr(self):
        print(self.name,self.email,self.role)

    def settr(self,new_mail):
        self.email=new_mail

    def print_info(self):
        print('{0}({1}) at {2}'.format(self.name,self.role,self.email))


class software_lab(lab):

    def __init__(self,name,role,email,scored_marks):
        super(software_lab,self).__init__(name,email,role)
        self.marks=scored_marks

    def print_marks(self):
        if self.role=='S':
            print(' {0}(S) scored {1} '.format(self.name,self.marks))
        else:
            print(' {0}(I) can be reached at {1} '.format(self.name,self.email))

s1=software_lab('Hrishi','S','jtm202055@iitd.ac.in',45)
i1=software_lab('Subrat_Kar','I','subratkar@ee.iitd.ac.in',0)
s1.gettr()
s1.print_info()
s1.settr('hrishikeshsaste@gmail.com')
s1.print_info()
s1.print_marks()
i1.print_marks()








    



        
           