#Game-Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False #if player's hand is still being played
outcome = ""
report = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank
    def __str__(self):
        return self.suit + self.rank
    def get_suit(self):
        return self.suit
    def get_rank(self):
        return self.rank
    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
# define hand class
class Hand:
    def __init__(self):# create Hand object-the field for storing Card objects
        self.cardlist = list()	
    def __str__(self):# return a string representation of a hand
        s = "Hand contains "
        for i in range(len(self.cardlist)):    
            s += str(self.cardlist[i]) +" "
        return s           
    def add_card(self, card):# add a card object to a hand
        self.cardlist.append(card)	
    def get_value(self):
        key_of_cards = list()
        value_of_cards = list() 
        for card in self.cardlist:
            cardkey = card.rank
            value_of_cards.append(VALUES[cardkey])
        handvalue = sum(value_of_cards) #handvalue is the sum of card value with Aces as 1
        for card in self.cardlist:
            cardkey = card.rank
            key_of_cards.append(cardkey)
        if 'A' not in key_of_cards:
            return handvalue
        else:
            if handvalue + 10 <=21: #count Aces as 1, if dont bust, add 10 to hand value
                return handvalue + 10
            else:
                return handvalue
    def draw(self, canvas, pos):
        i = 0
        for card in self.cardlist:
            card.draw(canvas,[pos[0]+(CARD_SIZE[0]+20)*i, pos[1]])
            i += 1
# define deck class 
class Deck:
    def __init__(self): #create a Deck object-the field for storing a list of Card objects
        self.deckcards = list()
        for suit in SUITS:
            for rank in RANKS:
                self.deckcards.append(Card(suit,rank))
    def shuffle(self):# shuffle the deck 
        random.shuffle(self.deckcards)    
    def deal_card(self):# deal a card object from the deck
        chopcard = self.deckcards[-1]
        self.deckcards.pop(-1)	
        return chopcard           
    def __str__(self):#return a string representing the deck
        s ="Deck contains "
        for i in range(len(self.deckcards)):    
            s += str(self.deckcards[i]) +" "
        return s 

#define event handlers for buttons
new_deck = Deck()
player_hand = Hand()
dealer_hand = Hand()
def deal():
    global outcome, in_play, new_deck, player_hand, dealer_hand, score, report
    report = "" #get rid of the reporting message for a new game
    if in_play == True:
        score -= 1
    else:
        new_deck = Deck() #shuffle a new deck each time
        player_hand = Hand() #new hand cards for both player and dealer
        dealer_hand = Hand()
        new_deck.shuffle()
        p1 = new_deck.deal_card()
        p2 = new_deck.deal_card()
        d1 = new_deck.deal_card()
        d2 = new_deck.deal_card()
        player_hand.add_card(p1)
        player_hand.add_card(p2)
        dealer_hand.add_card(d1)
        dealer_hand.add_card(d2)
        print "player's cards are", p1, p2, '\n',"dealer's cards are", d1, d2,'\n', "the cards left in deck are", new_deck
        print "there are", len(new_deck.deckcards), "cards left"
        in_play = True
        outcome = "Hit or Stand?" 
    
def hit():
    global in_play, outcome, score, report
    if in_play == True: # if the hand is in play, hit the player
        if player_hand.get_value() <= 21:
            p_extra = new_deck.deal_card()
            player_hand.add_card(p_extra)
            print "the player's value is", player_hand.get_value(),"now"
            if player_hand.get_value() > 21: 
                print "You have busted" # if busted, assign a message to outcome, update in_play and score
                in_play = False
                outcome = "New deal?"
                report = "You lose!"
                score -= 1  
                
def stand():
    global outcome, in_play, score, report
    if player_hand.get_value > 21:
        print "the player have busted"
        in_play = False
        score -= 1 
        report = "You lose!"
    else:
        while dealer_hand.get_value() < 17: # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
            d_extra = new_deck.deal_card()
            dealer_hand.add_card(d_extra)
        if dealer_hand.get_value() > 21:
            print " The dealer have busted"
            in_play = False
            score += 1
            report = "You won!"
        else:
            if player_hand.get_value() <= dealer_hand.get_value():
                print " The dealer won!"
                score -= 1
                report = "You lose!"
            else:
                print "The player won!"
                score += 1
                report = "You won!"
            in_play = False    
    outcome = "New deal?" # assign a message to outcome, update in_play and score
    
# draw handler    
def draw(canvas):
    global in_play
    player_hand.draw(canvas, [150, 350]) #to draw player's hand
    dealer_hand.draw(canvas, [150, 200]) #to draw dealer's hand
    canvas.draw_text(outcome, [220, 160], 30, 'Black')
    canvas.draw_text(report, [250, 520], 30, 'black')
    canvas.draw_text("Score:" + str(score), [450, 160], 30, 'black')
    canvas.draw_text("Blackjack", [200, 100], 50, 'lightblue')
    canvas.draw_text("Dealer", [30, 250], 30, "black")
    canvas.draw_text("Player", [30, 400], 30, "black") 
    if in_play == True: #if in play, hide dealer's first card
        pos = [150, 200]
        card_loc = (CARD_CENTER[0], CARD_CENTER[1] )
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)   
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
