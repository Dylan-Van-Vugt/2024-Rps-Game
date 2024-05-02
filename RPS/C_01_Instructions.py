# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure its lowercase
        user_response = input(question).lower()


        for item in valid_ans:
            # Check if the user response is a word in the list
            if item == user_response:
                return item

            # Check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # Print error if user does not enter a valid answer
        print(error)
        print()



def instructions():
    print('''
    
*** Instructions ***
    
To begin, choose the number of rounds (or choose infinite mode).

Then play against the computer. You need to choose paper, scissors, or rock.

The rules are as follows:
o   Paper beats rock
o   Rock beats scissors
o   Scissors beats paper

Press <xxx> to end the game at any time.

Good Luck
    ''')


# Main Routine
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()

# loop for testing purposes
while True:

    want_instructions = string_checker("Do you want to read the instructions? ")

    # checks users enter yes (y) or no (n)
    if want_instructions == "yes":
        instructions()

    print("program continues")
