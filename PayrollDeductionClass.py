class Payroll:

    def __init__(self, Description, Date, Charge, EmployeeID):

        self.description = Description
        self.date = Date
        self.charge = Charge
        self.id = EmployeeID

    def set_description(self, Description):
        self.description = Description

    def set_date(self, Date):
        self.date = Date
    
    def set_charge(self, Charge):
        self.charge = Charge
    
    def set_id(self, id):
        self.id = id

    def get_description(self):
        return self.description

    def get_date(self):
        return self.date
    
    def get_charge(self):
        return self.charge 
    
    def get_id(self):
        return self.id