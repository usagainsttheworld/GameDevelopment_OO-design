# "Stopwatch: The Game"

#Import Medules
import simplegui

# Global state
counter=0
interval=100
no_of_stops=0
stop_on_second=0
status=0 #Boolean variable that is 1 when stopwatch rnning and 0 when stopwatch stopped

# define helper function format that converts time
def format(t):
    global msecond
    minute = t//600
    if minute >=1:
        second = (t-(t//600)*600)//10
    else:
        second = t //10    
    msecond=t-minute*600-second*10   
    if second <= 9:
        return str(minute) + ":" + "0"+ str(second) +"." + str(msecond)
    else:
        return str(minute) + ":" + str(second) +"." + str(msecond)
       
# define event handlers for buttons; "Start", "Stop", "Reset"
def start ():
    global status
    status=1
    timer.start()
def stop ():
    global status, no_of_stops, stop_on_second 
    if status ==1:
        status=0 #set status back to 0 so that futher hitting stop button does not change score when game stopped   
        timer.stop()
        no_of_stops += 1
        if msecond == 0:
            stop_on_second += 1 
                 
def reset ():
    global counter, no_of_stops, stop_on_second 
    timer.stop()
    counter=0
    status=0
    no_of_stops=0
    stop_on_second=0
    
# define event handler for timer with 0.1 sec interval
def tick ():
    global counter
    counter += 1 
    #print counter
    
# define draw handler
def draw (canvas):
    canvas.draw_text(format(counter), (90, 110), 50, "Red")
    canvas.draw_text(str(stop_on_second)+"/"+ str(no_of_stops), (230, 30), 25, "Red")

# create frame
frame = simplegui.create_frame('stopwatch', 300, 200)

# register event handlers
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw)
button1 = frame.add_button('Start', start)
button2 = frame.add_button('Stop', stop)
button3 = frame.add_button('Reset', reset)

# start frame
frame.start()


