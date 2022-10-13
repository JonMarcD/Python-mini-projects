#Takes score input and outputs grade
 
inp = input('Enter given score between 0.0-1.0:\n')

#exception so that only numbers can be the input
try:
    final_grade = float(inp)
except:
    print('Please enter number.')

#chained conditional that excludes numbers which are not in the range
if final_grade < 0.0:
    print('Enter given score between 0.0-1.0')
elif final_grade > 1.0:
    print('Please enter score which is in range.')

#chained conditional which has the number range and their respective grade
if final_grade >= 0.9 and final_grade <= 1.0:
    print('grade = A')
elif final_grade >= 0.8 and final_grade <=0.85:
    print('grade = B')
elif final_grade >= 0.7 and final_grade <= 0.75:
    print('grade = C')
elif final_grade >= 0.6 and final_grade <= 0.65:
    print('grade = D')
elif final_grade < 0.6 and final_grade >= 0.0:
    print('grade = F')
