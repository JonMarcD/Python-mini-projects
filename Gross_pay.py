#Exercise 3: 

prompt1 = 'How many hours did you work?\n'
hours = input(prompt1)
prompt2 = 'At what rate did you work?\n'
rate = input(prompt2)
#Have to write float any input value can be a decimal which is not an integer
pay = float(hours) * float(rate)
print(pay)