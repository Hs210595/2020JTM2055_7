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


s1=lab('Hrishi','jtm202055@iitd.ac.in','S')
s1.print_info()


    



        
           