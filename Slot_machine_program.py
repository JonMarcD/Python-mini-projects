import random


#global constant done in all capitals
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
#values for the symbols of the slot machine
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#generates the outcome of the slot machine using values
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
#.items gives you both the key and value which is associated with the dictionary key = being symbol, value = being symbol_count
    for symbol, symbol_count in symbols.items():
#underscore is an anonomous variable
        for _ in range(symbol_count):
            all_symbols.append(symbol)
        
    columns = [] #define column
    for _ in range(cols): #generate column for every column we have
#this picks any random value for each row in our column
        column = []
#[:] creates a copy of the list all_symbols which doesn't directly affect the original
        current_symbols = all_symbols[:] #our all_symbols is equal to a copy of current symbols
        for _ in range(rows): #loop through number of values we need to generate = to number of rows
            value = random.choice(current_symbols) #picks random values
            current_symbols.remove(value) #this is so the same value isn't picked again
            column.append(value) #we add value ot our column
#
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])): #loop through every row we have and for every row we print the column for every column we print the one were on
#enumertate gives your the index as you loop through as well as the item
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ") #end tells print statement what to end the line with end = \n but instead it prints | at the end
            else:
                print(column[row], end="")


        print()#adding this just prints a new line but its empty so we can;t see it
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

#generates the slop machine
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()
