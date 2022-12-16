#Define a switch case to convert roman numeral to appropriate integer value
roman_table = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}

def roman_to_integer(s):
    total = 0                                         #Initialize total to 0
    last_value = "I"                                  #Assume the last value in a roman numeral will be 'I'

    for i in reversed(s):                             #Iterate over every character in string s in reversed order
        if roman_table[i] < roman_table[last_value]:  #If the current value is smaller than the previous
            total -= roman_table[i]                   #Subtract the current value from the total
        else:                                         #If the current value is larger than the previous
            total += roman_table[i]                   #Add it to the total

        last_value = i                                #Assign the last variable to the current index

    return total                                      #Return the total

user_input = input("Enter the roman numeral you would like to convert: ") #Obtain user input
user_input = user_input.upper()                                           #Convert user input to all caps
print(roman_to_integer(user_input))                                       #Call the roman_to_integer function
