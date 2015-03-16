# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
def name_to_number(name):
    # delete the following pass statement and fill in your code below
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name=="rock":
        number=0
    elif name=="Spock":
        number=1
    elif name=="paper":
        number=2
    elif name=="lizard":
        number=3
    elif name=="scissors":
        number=4
    else:
        print "Invalid input"
    return number
def number_to_name(number):
    # delete the following pass statement and fill in your code below
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number==0:
        name="rock"
    elif number==1:
        name="Spock"
    elif number==2:
        name="paper"
    elif number==3:
        name="lizard"
    elif number==4:
        name="scissors"
    else:
        print "Invalid number"
    return name   
def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    print "     "
    print "The player choose: "+player_choice
    player_number = name_to_number(player_choice)
    import random
    comp_number = random.randrange(0,5)
    comp_choice =number_to_name(comp_number)
    print "The computer choose: "+comp_choice
    diff = (player_number-comp_number) % 5
    if diff == 0:
        print"Player and computer tie!"
    elif diff <= 2:
        print"Player wins!"
    else:
        print"Computer wins!"
    
        
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


