import EmployeeClass as ec
import PayrollDeductionClass as pd

def main():

    my_emp = ec.Employee('Jimmy Smith', 58475, 'Information Systems','Developer', 6800 )

    #print('Name ,ID Number , Department, Job Title, Monthly Salary')
    print(f"{my_emp.get_name()}, {my_emp.get_id()}, {my_emp.get_department()}, {my_emp.get_title()}, {my_emp.get_salary():,.2f}")

    charge_01 = pd.Payroll('food court','8/14/2022', 22.50, 39119 )
    charge_02 = pd.Payroll('gift contribution','8/12/2022', 25.00, 58475 )
    charge_03 = pd.Payroll('food court','8/17/2022', 15.25, 21547 )
    charge_04 = pd.Payroll('vending machine','8/22/2022', 3.00, 58475 )
    charge_05 = pd.Payroll('vending machine','8/5/2022', 2.75, 58475 )

    #print('Name ,ID Number , Department, Job Title, Monthly Salary')
    print(f"{charge_01.get_description()}, {charge_01.get_date()}, {charge_01.get_charge():,.2f}, {charge_01.get_id()}")
    print(f"{charge_02.get_description()}, {charge_02.get_date()}, {charge_02.get_charge():,.2f}, {charge_02.get_id()}")
    print(f"{charge_03.get_description()}, {charge_03.get_date()}, {charge_03.get_charge():,.2f}, {charge_03.get_id()}")
    print(f"{charge_04.get_description()}, {charge_04.get_date()}, {charge_04.get_charge():,.2f}, {charge_04.get_id()}")
    print(f"{charge_05.get_description()}, {charge_05.get_date()}, {charge_05.get_charge():,.2f}, {charge_05.get_id()}")

    chargers = [charge_01, charge_02,charge_03,charge_04,charge_05]

    total_deduction = 0
    
    for line in chargers:

        if my_emp.get_id() == line.get_id():

            total_deduction += line.get_charge()

        net_salary = my_emp.get_salary() - total_deduction

    print(f"Net Salary: {net_salary:,.2f}")

main()


