import InsectClass as i

def main():

    mosquito = i.Insect(2,4,'mosquito')
    housefly = i.Insect(2,6,'housefly')

# Calculate the flight length

    mosquito.cal_flight()
    housefly.cal_flight()

# print the flight lenght

    print(f"The {mosquito.get_name()} can fly upto {mosquito.get_fight()} miles")
    print(f"The {housefly.get_name()} can fly  upto {housefly.get_fight()} miles")

main()