#A while loop that starts at the last character in the string printing each letter on a separate line, except backwards.

prompt = print("Enter a word with 8 characters.")
inp = input()

def error_handling():
    data = inp
    try:
        if any(i.isdigit() for i in data):
            raise ValueError('No integers')
    except ValueError as e:
        print(e)
        return print
    return data

def main():
    inp = error_handling()
    index = -1 #this sets the index as -1 so that it when the input is read it starts at the last letter
    while index < len(inp): #this statement is always true until the entire word is printed then the index will = character the statement will then become false
        letter = inp[index] #this says the index of the input and gives letter a definition
        if error_handling() == (print):
            break
        print(letter), #prints the letter
        index = index -1 #this just reads the word backwards allowing it to  be printed 
main()

