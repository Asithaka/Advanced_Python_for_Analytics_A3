import StudentClass as sc

def main():

    pick_sid = input('Enter your student id: ')

    pick_name = input('Enter your name: ')

    pick_DOB = input('Enter your date of birth (MM/DD/YYYY): ')

    pick_classification = input('Enter your classification (F, S, Jr, Sr): ')

    my_student = sc.Students(pick_sid, pick_name, pick_DOB, pick_classification)

    my_student.set_age()
    my_student.set_register_date()

    print(f'Your age is : {my_student.get_age()} and you can register from {my_student.get_date()}')

main()
