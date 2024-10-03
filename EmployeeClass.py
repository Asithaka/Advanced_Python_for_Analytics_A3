class Employee:

    def __init__(self, Name, ID, Department, Job_Title, Monthly_salary ):

        self.name = Name
        self.id = ID
        self.department = Department
        self.title = Job_Title
        self.salary = Monthly_salary

    def set_name(self, name):
        self.name =name

    def set_id(self, ID):
        self.id = ID
    
    def set_id(self, Department):
        self.department = Department
    
    def set_id(self, Job_Title):
        self.title = Job_Title

    def set_id(self, Monthly_salary):
        self.salary = Monthly_salary

    def get_name(self):
        return self.name 

    def get_id(self):
        return self.id 
    
    def get_department(self):
        return self.department 
    
    def get_title(self):
        return self.title 

    def get_salary(self):
        return self.salary 