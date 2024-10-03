class Payroll:

    def __init__(self, Description, Date, Charge, EmployeeID):

        self.__description = Description
        self.__date = Date
        self.__charge = Charge
        self.__id = EmployeeID

    def set_description(self, Description):
        self.__description = Description

    def set_date(self, Date):
        self.__date = Date
    
    def set_charge(self, Charge):
        self.__charge = Charge
    
    def set_id(self, id):
        self.__id = id

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date
    
    def get_charge(self):
        return self.__charge 
    
    def get_id(self):
        return self.__id