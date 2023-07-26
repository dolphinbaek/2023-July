"""price = 24
half_price = price/2
print(half_price)
"""

"""
is this
multi-line comment
working?
"""

# cool, it seems to be working. this is a single line comment


# PassiveAggressiveDivideByTwo! - a passive aggressive tool that asks what number user would like to see divided by two. 
# Input takes a number, output gives the input number divided by two after a snarky question.

# user inputs number
user_number_to_divide = input("So... What number would you like to divide in half?: ") #might be fun to add a little pause between the dialogues

#asks a silly question
silly_question = input("Do you have a calculator on you?: (Y/N) ")

#converting str input to int & simple division by 2
number_in_int = int(user_number_to_divide)
half = number_in_int/2
half_in_str = str(half)

#answers
if silly_question == "N": #find out how to add in an option to allow lowercase n as well, same with y
    print("*sigh* The answer is " + half_in_str + ", obviously.")
elif silly_question == "Y":
    print("...then just use your calculator.")
else:
    follow_up = input("At least answer the question correctly, will you?")
#add in looping feature

"""
ChatGPT answer for reference:
def divide_by_two():
    try:
        user_input = int(input("Enter an integer: "))
        result = user_input / 2
        print(f"{user_input} divided by 2 is: {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    divide_by_two()
"""




