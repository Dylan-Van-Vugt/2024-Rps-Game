import random

print()


# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=('yes', 'no')):
    error = f"\nPlease enter a valid option from the following list: {valid_ans}"

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


# Compares user and comp choices and says win or lose
def rps_compare(user, comp):
    if user == comp:
        round_result = "tie"

    elif user == "rock" and comp == "scissors":
        round_result = "win"
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "paper" and comp == "rock":
        round_result = "win"

    else:
        round_result = "lose"

    return round_result


# Main Routine starts here


# Initialize game variables
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0
rounds_won = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print(" ***  Rock / Paper / Scissors  *** ")
print()

# Instructions

want_instructions = string_checker("Do you want to read the instructions? ")
print()

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / inf mode
num_rounds = int_check("How many rounds would you like to play? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n **  Round {rounds_played + 1} (Infinite Mode)  ** "
    else:
        rounds_heading = f"\n **  Round {rounds_played + 1} of {num_rounds}  ** "

    print(rounds_heading)
    print()

    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    user_choice = string_checker("Choose: ", rps_list)
    print("You chose", user_choice)

    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    if result == "tie":
        rounds_tied += 1
        feedback = " ** Its a Tie ** "

    elif result == "win":
        rounds_won += 1
        feedback = " ** You Win ** "
    else:
        feedback = " ** You Lost ** "
        rounds_lost += 1

    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played + 1} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1


    # If users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game history/ stats
if rounds_played > 0:
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    print()
    print()
    print(" ***  Game Stats  *** ")
    print(f" * Won: {percent_won:.2f} * \t "
          f" * Lost: {percent_lost:.2f} * \t "
          f" * Tied: {percent_tied:.2f} *")
    print()

    show_history = string_checker("Do you want to see the game history?")
    if show_history == "yes":
        print("\n *** Game History *** ")

        for item in game_history:
            print(item)

        print()

else:
    print(" *** Oops - You chickened out! *** ")
