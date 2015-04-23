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

#Quiz 5a
#Q9
mylist = [0, 1]
for i in range(0, 40):
    mylist.append(sum([mylist[-1], mylist[-2]]))
print mylist

#Quiz 6a
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.fee = 0
        """Creates an account with the given balance."""
    def deposit(self, amount):
        self.balance = self.balance + amount
        """Deposits the amount into the account."""
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < 0:
            self.balance = self.balance - 5
            self.fee = self.fee + 5
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fee
account1 = BankAccount(10)
account1.withdraw(15)
account2 = BankAccount(15)
account2.deposit(10)
account1.deposit(20)
account2.withdraw(20)
print account1.get_balance(), account1.get_fees(), 
      account2.get_balance(), account2.get_fees()

#Quiz 6b
#Q7 keep only prime number in the list
n = 1000
numbers = range(2, n)
result = []
while len(numbers) > 0:
    result.append(numbers[0])
    numbers = [n for n in numbers if n % numbers[0] != 0]
print len(result)

#Q8 by which year fast worm outnumber slow worm
def Wump(slow, fast):
    i = 1
    while slow > fast:
        slow = slow*2
        slow = slow *0.6
        fast = fast *2
        fast = fast *0.7
        i = i+1
        print "in year", i, "slow is:", slow, "fast is:", fast
     
Wump(1000, 1)   

###########################################
#Quiz 7a
#Q1
class Point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def translate(self, deltax = 0, deltay = 0):
        """Translate the point in the x direction by deltax
           and in the y direction by deltay."""
        self.x += deltax
        self.y += deltay
point1 = Point2D(3, 9)
point2 = Point2D()
point2.translate(20, 4)  

#Q2
class Point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def translate(self, deltax = 0, deltay = 0):
        """Translate the point in the x direction by deltax
           and in the y direction by deltay."""
        self.x += deltax
        self.y += deltay
point0 = Point2D(2, 5)
point1 = Point2D(8, 3)
point2 = Point2D(0, 2)
points = [point0, point1, point2]
for point in points:
    point.translate(-1, -1)

########################################
#Quiz 8
#Q8 How many distinct numbers are printed by the following code? Enter the count.

'''def next(x):
    return (x ** 2 + 79) % 997

x = 1
for i in range(1000):
    print x
    x = next(x)'''

def next(x):
    return (x ** 2 + 79) % 997

x = 1
s=set([])
for i in range(1000):
    #print x
    s.add(x)
    x = next(x)
print len(s)




    
                     












