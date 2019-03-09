import parking

spots = [0] * 4

def loop():
    while True:
        choice = input("Hi, welcome to our valet system. What would you like to do today?")
        if choice == "Park":
            location = input("Where would you like to park?")
            if spots[(int(location) - 1)] == 0:
                parking.park()
            else:
                print("Sorry, that spot is taken!")
        elif choice == "Leave":
            #temp
            print("Do something")
        else:
            print("You cannot do that here. Please try again.")

if __name__ == "__main__":
    loop()