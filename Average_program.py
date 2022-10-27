 #Program takes numbers input by the user and prints out count, total, average

def main(): #where the program runs
    count = 0
    total = 0
    while True: #a loop which checks if the following statements are true
        inp = input("Enter number then write done when finished. ")
        data = inp
        if data == "done": #this just checks if data is equal to done which is the only acceptable string
            break
        try:
            data = int(inp)
        except:
            if data != int: #if data isn't an integer it runs the if statement
                print("Bad data. Please write number")
                continue
        count = count + 1
        total = total + data
    print(f"Computation done. Count: {count}. Total: {total}. Average: {total/count}")

main()
