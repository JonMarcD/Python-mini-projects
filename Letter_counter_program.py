#Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

try: #exceptions
    print("Enter word.")
    word = input()
    if any(i.isdigit() for i in word): #this just checks if there is an integer in the variable word and we are invoking that integer can be any digit with (i.isdigit())
        raise ValueError('Error no integers.') #if the statement is true this ValueError is raised
    print("Now enter letter you would like to be counted.") #if the previous statement was false it continues and ask for another input
    inp_letter = input()
except ValueError as e:
    print(e)

def counter(word, inp_letter): #takes in 2 arguments
    count = 0
    for letter in word: #does a loop for letter in the variable word
        if letter == inp_letter: #this checks if any of the letters in word are the same as the inp_letter
            count = count + 1 #if there are any letters in the word which are the same as the letter_inp it adds to the count how many letters there were.
    return count

print(f"This is the count for the letter {inp_letter}: {counter(word, inp_letter)}.")
