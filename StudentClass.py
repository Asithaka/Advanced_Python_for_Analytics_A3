
import datetime

class Students:

    def __init__(self, StudentID, Name, DOB,Classification):

        self.StudentID = StudentID
        self.Name = Name
        self.DOB = DOB
        self.Classification = Classification

    def set_age(self):
           
        today = datetime.date.today()

        current_yr = today.year

        birth_yr = int(self.DOB.split('/')[2])

        age = current_yr - birth_yr

        self.age=age

    def set_register_date(self):

        if self.Classification == 'Sr':

            self.reg_date = '4/1 thru 4/3'

        elif self.Classification == 'Jr':

            self.reg_date = '4/4 thru 4/6'

        elif self.Classification == 'S':

            self.reg_date = '4/7 thru 4/9'

        elif self.Classification == 'F':

            self.reg_date = '4/10 thru 4/12'
        else:
            self.reg_date = 'Classification is not valid'

    def get_age(self):
        return self.age
    
    def get_date(self):
        return self.reg_date