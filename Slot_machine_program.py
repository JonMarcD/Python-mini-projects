#global constant done in all capitals
MAX_LINES = 3

#Function to collect deposite through user input
def deposite():
#while loop continually ask user for a amount until it is a registered valid amount
    while True:
        amount = input("What would you like to deposit? $")
#checks if the input is an integer through nested conditional
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a number.")
    return amount

#collect bet from user
def get_number_of_lines():


#where the main program will be in
def main():
    balance = deposite()

main()
