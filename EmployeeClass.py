class Employee:

    def __init__(self, Name, ID, Department, Job_Title, Monthly_salary ):

        self.__name = Name
        self.__id = ID
        self.__department = Department
        self.__title = Job_Title
        self.__salary = Monthly_salary

    # def set_name(self, name):
    #     self.__name =name

    # def set_id(self, ID):
    #     self.__id = ID
    
    # def set_department(self, Department):
    #     self.__department = Department
    
    # def set_title(self, Job_Title):
    #     self.__title = Job_Title

    # def set_salary(self, Monthly_salary):
    #     self.__salary = Monthly_salary

    def get_name(self):
        return self.__name 

    def get_id(self):
        return self.__id 
    
    def get_department(self):
        return self.__department 
    
    def get_title(self):
        return self.__title 

    def get_salary(self):
        return self.__salary 