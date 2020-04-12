# Store saponification amounts for later

coconut_lye = 0.1910
olive_lye = 0.1353

# Make a function to ensure that measurements are entered as numbers, not strings

def input_measurements(question):
    while True:
        try:
            userInput = float(input(question))
        except ValueError:
            print("Please input a number\n")
            continue
        else:
            return userInput
        break

# Make a function to ensure that we get a proper yes/no answer to our question (accept variations on these answers)
    
def yes_no(question):
    yes = set(['yes','y', 'ye', 'yep'])
    no = set(['no','n', 'nope'])
     
    while True:
        choice = input(question).lower()
        if choice in yes:
           return True
        elif choice in no:
           return False
        else:
            print("Please respond with 'yes' or 'no'\n")

# Make a function to ensure we get a number between 1-10

def percentage(question):
    while True:
        userInput = input_measurements(question)
        if userInput < 1 or userInput > 10:
            print("Please input a number between 1 and 10\n")
            continue
        else:
            return userInput
        break
    
print("Welcome to the soap calculator. Please follow the instructions onscreen to get started.\n")

# Get olive oil measurements and store this as a variable

olive_oil = input_measurements("Please enter the amount of olive oil you would like to use in grammes.\n")

print("Okay, {O}g of Olive Oil\n".format(O = olive_oil))

# Get coconut oil measurements and store this as a variable

coconut_oil = input_measurements("Please enter the amount of coconut oil you would like to use in grammes.\n")

print("Okay, {C}g of Coconut Oil.\n".format(C = coconut_oil))

# Check if the user wants to reduce their lye content

use_reduction = yes_no("Would you like to use lye reduction?\n")

# If the user chooses to reduce their content, get a percentage between 1 - 10

if use_reduction:
    lye_reduction = percentage("Please enter the percentage of reduction you would like to use (between 1 and 10)\n")

# Calculate the total values and return them to the user
    
water_needed = (coconut_oil + olive_oil) / 3
if use_reduction:
    coconut_lye = coconut_lye - ((lye_reduction/100) * coconut_lye)
    olive_lye = olive_lye - ((lye_reduction/100) * olive_lye)

coconut_lye_needed = coconut_oil * coconut_lye
olive_lye_needed = olive_oil * olive_lye
    
lye_needed = coconut_lye_needed + olive_lye_needed

print("For {O}g of Olive Oil and {C}g of Coconut Oil, you will need:\n* {W:.3f}ml of water\n* {L:.3f}g of lye".format(O = olive_oil, C = coconut_oil, W = water_needed, L = lye_needed))
