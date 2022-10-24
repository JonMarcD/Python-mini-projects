 #Program takes numbers input by the user and prints out count, total, average
from operator import truediv

#this takes the input and checks if its an legal variable which can be used
def input_source():
    inp = input("Enter number then write done when finished. ")
    try:
        data = inp
        if data == "done": #this just checks if data is equal to done which is the only acceptable string
            return data
        data = int(data) #this makes almost all acceptable values only integers
    except:
        if data != int: #if data isn't an integer it runs the if statement
            print("Bad data. Please write number")
    return data #this is whats returned from the function

def main(): #where the program runs
    while True: #a loop which checks if the following statements are true
        data = input_source() #defines the variable data as input source
        if data == int: #this checks the data to be an integer and continues the loop
            continue
        if data == "done": #if data is the string "done" it stops the loop stoping the program
            break
    print("Computation done.")

main()
