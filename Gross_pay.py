#Gross pay program:
#Has to be at the start because of flow execution
prompt1 = print("How many hours did you work?")
int = input()

#function that calculates pay the parameters get are the input to the equation inside the function
def computepay(hours, rate):
    pay = float(hours) * float(rate) #hours & rate take whatever is set as the parameter
    return pay #the return statement is sent to the calling code and used as the functions result

def overtimepay(hours, rate):
    ot_pay = float(hours) * float(rate)
    return ot_pay

try:
    hours = float(int)
    rate = 10
    full_hours = float(40)
    if hours > full_hours: #short circuited if not true doesn't continue and moves to except:
        ot_hours = float(hours) - full_hours
        ot_rate = 15
        ot_gross = overtimepay(ot_hours, ot_rate) + computepay(full_hours, rate)
        print(f"${ot_gross} is your gross pay.")
    else:  #nested conditional
        if hours <= full_hours:
            pay = computepay(int, rate)
        print(f"${pay} is your gross pay.")
except:
    print("Error, please enter numeric input")

#ot_pay = float(ot_hours) * float(ot_rate)