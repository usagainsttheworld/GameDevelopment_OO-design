# "Pong"

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
red_score = 0
green_score =0
# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos=[WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction): 
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240)/60, -random.randrange(60, 180)/60]
    if direction == LEFT:
        ball_vel = [-random.randrange(120, 240)/60, -random.randrange(60, 180)/60] 
   
# define event handlers
def new_game():
    global ball_pos, ball_vel, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global red_score, green_score  # these are ints
    red_score = 0
    green_score = 0 
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    ball_pos=[WIDTH/2, HEIGHT/2]
    ball_vel = [0, 0]
    spawn_ball(RIGHT if random.randint(0,1) == 1 else LEFT)    

def draw(canvas):
    global paddle1_pos, paddle2_pos,paddle1_vel, paddle2_vel, ball_pos, ball_vel, red_score, green_score    
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White") 
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")  

    # collides with top/bottom 
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT-BALL_RADIUS:
       ball_vel[1] = -ball_vel[1]
 
    # collides with left/right 
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
        if ball_pos[1] < (paddle1_pos - PAD_HEIGHT) or ball_pos[1] > (paddle1_pos+PAD_HEIGHT): 
            spawn_ball(RIGHT)
            green_score +=1      
        else:
            ball_vel[0] = -ball_vel[0]*1.1
    if ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] < (paddle1_pos - PAD_HEIGHT) or ball_pos[1] > (paddle1_pos+PAD_HEIGHT): 
            spawn_ball(LEFT)
            red_score +=1
        else:
            ball_vel[0] = -ball_vel[0]*1.1
        
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if paddle1_pos < (HALF_PAD_HEIGHT) and paddle1_vel< 0:
        paddle1_vel = 0
    elif paddle1_pos > (HEIGHT - HALF_PAD_HEIGHT) and paddle1_vel> 0:
        paddle1_vel = 0  
    if paddle2_pos < (HALF_PAD_HEIGHT) and paddle2_vel< 0:
        paddle2_vel = 0
    elif paddle2_pos > (HEIGHT - HALF_PAD_HEIGHT) and paddle2_vel> 0:
        paddle2_vel = 0     
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, (paddle1_pos - HALF_PAD_HEIGHT)], [HALF_PAD_WIDTH, (paddle1_pos + HALF_PAD_HEIGHT)], PAD_WIDTH, "Red")
    canvas.draw_line([(WIDTH - HALF_PAD_WIDTH), (paddle2_pos - HALF_PAD_HEIGHT)], [(WIDTH - HALF_PAD_WIDTH), (paddle2_pos + HALF_PAD_HEIGHT)], PAD_WIDTH, "Green")
    
    # draw scores
    canvas.draw_text(str(red_score), (140, 70),60, 'Red')
    canvas.draw_text(str(green_score), (460, 70),60, 'Green')   

def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 3
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc  
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0  

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Reset', new_game)

# start frame
new_game()
frame.start()
