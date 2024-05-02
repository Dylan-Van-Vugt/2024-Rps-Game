# Checks for an integer that is more than 0
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more. "

        to_check = input(question)

        # Check for inf mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # Checks that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main Routine starts here


# Initialize game variables
mode = "regular"
rounds_played = 0

print(" ***  Rock / Paper / Scissors  *** ")
print()

# Instructions


# Ask user for number of rounds / inf mode
num_rounds = int_check("How many rounds would you like to play? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n ***  Round {rounds_played + 1} (Infinite Mode)  *** "
    else:
        rounds_heading = f"\n ***  Round {rounds_played + 1} of {num_rounds}  *** "

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # If users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game history/ stats
