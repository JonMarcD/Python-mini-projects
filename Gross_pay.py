#Gross pay program:
prompt1 = print("How many hours did you work?")
int = input()

try:
    hours = float(int)
    if float(hours) > float(40):
        rate = 15
    else:  #nested conditional
        if float(hours) <= float(40):
            rate =10
    pay = float(hours) * float(rate)
    print(f"${pay} is your gross pay.")
except:
    print("Error, please enter numeric input")