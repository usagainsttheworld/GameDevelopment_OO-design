#"Guess the number" mini-project
# helper function to start and restart the gamedef 
import random
import simplegui
#initialize global variables
n_guess=7
guess_range=100
secret_number=-1
# define event handlers for control panel
def range100():
    global n_guess
    global guess_range
    global secret_number
    n_guess=7
    guess_range=100
    secret_number=random.randrange(0,100)
    print "New game. Range is from 0 to 100."
    print "Number of remaining guesses is", n_guess,"\n"
    return secret_number 
def range1000():
    global n_guess
    global guess_range
    global secret_number
    n_guess=10
    guess_range=1000
    secret_number=random.randrange(0,1000)
    print "New game. Range is from 0 to 1000."
    print "Number of remaining guesses is", n_guess,"\n"
    return secret_number        
def input_guess(guess):
    global n_guess
    n_guess=n_guess-1
    if (n_guess==0):
        print "You ran out of guesses!"
        print "The number was",secret_number,"\n"
        reset()
    else:
        global guess_number
        guess_number=int(guess)
        print "Guess was", guess_number
        print "Number of remaining guesses is",n_guess
        if (guess_number == secret_number):
            print "Correct!\n"
            reset()
        elif (guess_number < secret_number):
            print "Higher!\n"
        else:
            print "Lower!\n"
#when the game ends, a new game with the same range as the last one begins
def reset():
    global guess_range
    if (guess_range==100):
        range100()
    else:
        range1000()
# register event handlers for control elements and start frame
import simplegui
frame=simplegui.create_frame("guess_the_number",200,200)
guess=frame.add_input("Please guess a number",input_guess,50)
frame.add_button("Range0-100",range100,100)
frame.add_button("Range0-1000",range1000,100)
# new game begin in range [0,100) 
frame.start()
range100()



