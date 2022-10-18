#Gross pay program:
prompt1 = print("How many hours did you work?")
int = input()

try:
    hours = float(int)
    if float(hours) > float(40):
        ot_hours = float(hours) - float(40)
        rate = 15
        ot_pay = float(ot_hours) * float(rate)
        normal_hours = float(40) * float(10)
        ot_gross = float(ot_pay) + float(normal_hours)
        print(f"${ot_gross} is your gross pay.")
    else:  #nested conditional
        if float(hours) <= float(40):
            rate =10
        pay = float(hours) * float(rate)
        print(f"${pay} is your gross pay.")
except:
    print("Error, please enter numeric input")