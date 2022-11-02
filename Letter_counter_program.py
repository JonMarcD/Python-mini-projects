#Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

print("Enter word.")
word = input()
print("Now enter letter you would like to be counted.")
inp_letter = input()

def counter(word, inp_letter):
    count = 0
    for letter in word:
        if letter == inp_letter:
            count = count + 1
    return count

print(f"This is the count for the letter {inp_letter}: {counter(word, inp_letter)}.")
