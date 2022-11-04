#This program will take a set string and slice it so that only the characters after the colon will be extracted and converted into a float.

data = 'X-DSPAM-Confidence:0.8475'

colon_pos = data.find(':') #this just finds the colon position and defines it as the variable colon_pos
print(colon_pos) #prints the colon position

sppos = data.find(' ',colon_pos) #this is suppose to find the first space but since there is no space it just gives us the position of the last character
print(sppos)

host = data[colon_pos+1:sppos] #this just tells us that the data were looking for is between the colon position and the position of the last character
print(host)