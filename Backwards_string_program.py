#A while loop that starts at the last character in the string printing each letter on a separate line, except backwards.

prompt = print("Enter a word with 8 characters.")
inp = input()
index = 0
while index < len(inp):
    letter = inp[index]
    print(letter)
    index = index - 1
