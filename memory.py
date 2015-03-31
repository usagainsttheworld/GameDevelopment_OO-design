#"Memory" Game

import simplegui
import random

numbers = [ ]
exposed = [ ]
index = 0
card_height = 100
card_width = 50
turns = 0
              
# helper function to initialize globals
def new_game():
    global numbers, exposed
    #generate number list for all 16 cards
    list1 = range(0,8)
    list2 = range(0,8)
    numbers = list1 + list2
    random.shuffle(numbers)
    #set exposed list to False for all cards
    for number in numbers:
        exposed.append(False) 

# define event handlers
def mouseclick(pos):
    global index, exposed
    card_pos = list(pos)
    index = card_pos[0]/50 
    if exposed[index] == False:
        print "the card number", index, "is flipped"
        exposed[index] == True
    else:
        return                          

# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, index, card_height, card_width 
    if exposed[index] == True:
        print"should expose number now"
        canvas.draw_text(str(numbers[index]), (index+10, 65), 50, "White")
    for index in range(0, 16):
        if exposed[index] == False:
            canvas.draw_line([card_width*index, 0],[card_width*index, card_height], 5, 'Grey')
            canvas.draw_line([card_width*(index+1), 0], [card_width*(index+1), card_height], 5, 'Grey')
            canvas.draw_line([index*card_width + card_width/2, 0], [index*card_width + card_width/2, card_height], 46, 'Green')
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric