import parking

spots = [0] * 4

def loop():
    while True:
        choice = input("Hi, welcome to our valet system. What would you like to do today? ")
        if choice == "Park":
            for i in spots:
                if spots[i] == 0:
                    id = input("What is the id of the car? ")
                    parking.park(id)
                    spots[i] = 1
                    break
        elif choice == "Leave Spot":
            location = input("Which spot was it? ")
            spots[int(location) - 1] = 0
        elif choice == "Leave":
            print("Thank you for chosing our system! We hope to see you again!")
            break
        else:
            print("You cannot do that here. Please try again.")

if __name__ == "__main__":
    loop()