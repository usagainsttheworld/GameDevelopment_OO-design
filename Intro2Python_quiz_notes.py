#Quiz 4b 
#which funciton must have global point declaration?
point = [0, 0]
def function1():
    point[0] += 1 #doesn't have to do global declaration when change elements
    point[1] += 2
function1()
print point
        
def function2():
    global point #has to do global declaration
    point = [50, 50]
function2()
print point
print "========"

#whether these three accomplish the same thing
#1
a = range(5)

def mutate(a):
    a[3] = 100

mutate(a)
print a[3]
#2
a = range(5)

def mutate(b):
    a[3] = 100

mutate(a)
print a[3]
#3
a = range(5)

def mutate(b):
    b[3] = 100

mutate(a)
print a[3]
print "========"

#Do the point and rectangle ever overlap?
import simplegui
width = 300
hight = 200
radius=5

point_pos = [10,20]
vel = [3, 0.7]
def timer_hander():
    point_pos[0] += vel[0]
    point_pos[1] += vel[1]    
def draw_handler(canvas):#!!!creat a time handler
    canvas.draw_circle(point_pos,radius, 2, "White")
    canvas.draw_polyline([(50, 50), (180, 50), (180, 140), (50,140)], 5, 'Red') 
    canvas.draw_polyline([(50, 50), (50,140)], 5, 'Red') 
    
frame = simplegui.create_frame("point goes to rectangle", width, hight)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100,timer_hander)
frame.start()
timer.start()#!!!start the timer!
print "========"

#change global variable by press key and release key
import simplegui
a = str(5) #!to draw on canvas, must convert to string first
def keydown(key):
    global a
    a = str(int(a)*2)#convert to intiger for calculation and change back to string for drawing
def keyup(key): 
    global a 
    a = str(int(a)-3)
    
def draw(canvas):
    canvas.draw_text(a, [50,50], 20, "Red")    
    
frame=simplegui.create_frame("keypress", 100,100)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

frame.start()

    
                     












