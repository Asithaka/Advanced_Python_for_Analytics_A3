import CellPhoneClass as cp

def main():

    cust_manufacture = input("Enter the name of the phone's manufacturer:")
    cust_model = input("Enter the name of model of the phone:")
    cust_price = input("Enter the price of the phone:")

    my_phone = cp.cellphone(cust_manufacture, cust_model, cust_price)

    #my_phone.set_manufact()
    #my_phone.set_model()
    #my_phone.set_retail_price()

    print(f"The the phone's manufacturer is {my_phone.get_manufact()}")
    print(f"The model of the phone is {my_phone.get_model()}")
    print(f"The price of the phone is {my_phone.get_retail_price()}")

main()