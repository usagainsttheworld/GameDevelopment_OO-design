#"Memory" Game

import simplegui
import random

numbers = [ ]
exposed = [ ]
index = 0
card_height = 100
card_width = 50
state = 0
card_fliped1 = 0
card_fliped2 = 0
turns = 0
           
# helper function to initialize globals
def new_game():
    global numbers, exposed, turns
    turns = 0
    exposed = [ ]
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
    global index, exposed, state, card_fliped1, card_fliped2, turns
    card_pos = list(pos)
    index = card_pos[0]/50
    if exposed[index] == False: #only response to mouseclick when card is not exposed
        if state == 0:
            exposed[index] = True
            state = 1
            card_fliped1 = index  
        elif state == 1:
            exposed[index] = True
            turns = turns + 1
            state = 2
            card_fliped2 = index
        else:
            if not numbers[card_fliped1] == numbers[card_fliped2]: #if the two previous card unpair
                exposed[card_fliped1] = False #flip them over
                exposed[card_fliped2] = False
            exposed[index] = True
            card_fliped1 = index #reset the fliped card1
            state = 1  

# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, index, card_height, card_width 
    label.set_text("Turns = " + str(turns)) #update the turns 
    for index in range(0, 16):
        if exposed[index] == True: #exposed is True, the card should face up with value visible
            canvas.draw_text(str(numbers[index]), (index*card_width+10, 65), 50, "White")  
        if exposed[index] == False: # exposed is False, the card should face down with value hidden
            canvas.draw_line([card_width*index, 0],[card_width*index, card_height], 5, 'Grey')
            canvas.draw_line([card_width*(index+1), 0], [card_width*(index+1), card_height], 5, 'Grey')
            canvas.draw_line([index*card_width + card_width/2, 0], [index*card_width + card_width/2, card_height], 46, 'Green')
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label('label')

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

