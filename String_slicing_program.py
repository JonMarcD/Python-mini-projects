#This program will take a set string and slice it so that only the characters after the colon will be extracted and converted into a float.

def colon_position(data):
    colon_pos = data.find(':') #this just finds the colon position and defines it as the variable colon_pos
    return colon_pos

def end_position(data, colon_pos):
    colon_pos = colon_position(data)
    end_pos = data.find(' ',colon_pos) #this is suppose to find the first space but since there is no space it just gives us the position of the last character
    return end_pos

def main():
    print("Data is = X-DSPAM-Confidence:0.8475")
    data = 'X-DSPAM-Confidence:0.8475'
    colon_pos = colon_position(data)
    end_pos = end_position(data, colon_pos)
    print(f"Colon position: {colon_pos}")
    print(f"End position: {end_pos}")
    host = data[colon_pos+1:end_pos] #this just tells us that the data were looking for is between the colon position and the position of the last character

    float_host = float(host) #this just takes the host and turns it into a float
    print(f"This is the information: {float_host}")
main()
