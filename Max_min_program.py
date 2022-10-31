#Write a program that prompts for a list of numbers as above and at the end prints out both the max and min of the numbers.

from gzip import BadGzipFile


def main():
    largest = None
    smallest = None
    while True:
        inp = input("Enter number. ")
        data = inp
        if data == "done":
            break
        try:
            data = int(data)
        except:
            if data != int:
                print("Bad data.")
                continue
        if largest is None or data > largest:
            largest = data
        if smallest is None or data < smallest:
            smallest = data
    print(f"Data maximum = {largest}, minimum = {smallest}.")
main()
