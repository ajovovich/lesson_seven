import re

#Task 1: Start

temp_input = input("Enter the degrees in Fahrenheit")

#Task 2: Temperature Conversion  
 
def conversion(temp_input):
    temp_input = int(temp_input)
    return (temp_input - 32) * 5/9

try:
    for temp in temp_input:
        if not re.fullmatch('.*[0-9]+', temp_input):
            print("Data inputed is cannot be converted to a number")
#Task 3: User Experience
    else:
        converted_temp = conversion(temp_input)
        print(f"{temp_input} degrees Fahrenheit is equal to {converted_temp:.2f} degrees Celsius")

except (ValueError):
    print("Thats not a number!")
#Task 4: Finally
finally:
    print("Thank you for using our weather converter")