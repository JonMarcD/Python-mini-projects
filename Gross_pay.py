#Gross pay program:

prompt1 = 'How many hours did you work?\n'
hours = input(prompt1)
if float(hours) > float(40):
    rate = 15
else:  #nested conditional
    if float(hours) <= float(40):
        rate =10

#Have to write float any input value can be a decimal which is not an integer
pay = float(hours) * float(rate)
print(f"${pay} is your gross pay.")