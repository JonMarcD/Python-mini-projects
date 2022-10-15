#global constant done in all capitals
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#ALl user input
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
            print("Please enter a number.")
    return amount

#collect bet from user
def get_number_of_lines():
    while True:
#Added global constant MAX_LINES
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("please enter a number.")
    return lines

#amount which is bet on each line
def get_bet(): 
    while True:
        amount = input("What would you line to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
#f-string to embed variables in the string without having to convert it into a string beforehand
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a number.")
    return amount

#where the main program will be in
def main():
#giving variables values
    balance = deposite()
    lines = get_number_of_lines()
#checks if your total bet on each line to make sure you didn't exceed disposited amount
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enought to bet that amount, your current balance is: ${balance} ")
        else:
            break

#printing what has been inputed back to the user
    print(f"You are betting ${bet} on {lines} llines. Total bet is equal to: ${total_bet} ")

main()
