import EmployeeClass as ec
import PayrollDeductionClass as pd

def main():

    my_emp = ec.Employee('Jimmy Smith', 58475, 'Information Systems','Developer', 6800 )

    print('Name ,ID Number , Department, Job Title, Monthly Salary')
    print(f"{my_emp.get_name}, {my_emp.get_id}, {my_emp.department}, {my_emp.get_title}, {my_emp.get_salary,.2f}")

    my_charge = pd.Payroll('food court',8/14/2022, 22.50, 39119 )
    my_charge = pd.Payroll('gift contribution',8/12/2022, 25.00, 58475 )
    my_charge = pd.Payroll('food court',8/17/2022, 22.50, 21547 )
    my_charge = pd.Payroll('vending machine',8/22/2022, 22.50, 58475 )
    my_charge = pd.Payroll('vending machine',8/5/2022, 22.50, 58475 )

    print('Name ,ID Number , Department, Job Title, Monthly Salary')
    print(f"{my_charge.description}, {my_charge.get_date}, {my_charge.charge, .2f}, {my_charge.get_id}")