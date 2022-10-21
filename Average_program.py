#Program takes numbers input by the user and prints out count, total, average
print("Enter number")

#def data_read(inp):
while True:
    data = input()
    if data[0] == '#':
        continue
    if data == "done":
        break
    print(data)
print("Done")

#this just checks if input is legal variable
#def input_check(inp):
try:
    data = int(data)
except:
    print("Bad data. Please write number")
