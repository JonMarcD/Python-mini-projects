#Takes score input and makes sure the input is a legal value
def scoreinput():
    inp = input('Enter given score between 0.0-1.0:\n')
    try:#exception so that only numbers can be the input
        score = float(inp)
        if score < 0.0:#chained conditional that excludes numbers which are not in the range
            print('Enter given score between 0.0-1.0')
        elif score > 1.0:
            print('Please enter score which is in range.')
    except:
        print('Please enter number.')
    return inp #if this function is called it returns inp

#Function that takes the score as a parameter and returns grade as string
def computegrade(score):
#A simple chained conditional
    if score >= 0.9 and score <= 1.0:
        grade = "A"
    elif score >= 0.8 and score <=0.85:
        grade = "B"
    elif score >= 0.7 and score <= 0.75:
        grade = "C"
    elif score >= 0.6 and score <= 0.65:
        grade = "D"
    elif score < 0.6 and score >= 0.0:
        grade = "F"
    return grade #this just returns the variable grade so if you call for the function the return is grade

#the main part of the program which defines the function scoreinput(): as score and prints out the grade associated with the score
def main():
    score = float(scoreinput())
    print(f"Final grade is {computegrade(score)}")

main()