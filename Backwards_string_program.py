#A while loop that starts at the last character in the string printing each letter on a separate line, except backwards.

prompt = print("Enter a word with 8 characters.")
inp = input()

def error_handling(): #this checks for any illegal variables
    data = inp
    try: #exceptions
        if any(i.isdigit() for i in data): #this checks if there are any integers in data and we are invoking that i can be any digit (i.isdigit())
            raise ValueError('No integers') #if this statement is true it raises a ValueError with a string
    except ValueError as e: #says to except ValueError
        print(e)
        return print #returns print as a value if this occurs the loop breaks in the main() function
    return data

def main():
    inp = error_handling() #defines inp as the function error_handling()
    index = -1 #this sets the index as -1 so that it when the input is read it starts at the last letter
    while index < len(inp): #this statement is always true until the entire word is printed then the index will = character the statement will then become false
        letter = inp[index] #this says the index of the input and gives letter a definition
        if error_handling() == (print): #checks if the value which is returned from error_handling() is print which will break the loop
            break
        print(letter), #prints the letter
        index = index -1 #this just reads the word backwards allowing it to  be printed 
main()

