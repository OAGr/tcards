import random
import pdb

class Card(object):
    def __init__(self, face, body, *tags):
        self.face = face
        self.body = body
        self.tags = tags
        self.difficult = 0
    def show__sequence(self):
        print 'this is ' + self.face
        input("press any char to see back")
        print self.body
        print self.tags
        difficult = input("how difficult was this for you?")
        self.difficult.append(difficult)

class Deck(object):
    def __init__(self):
        self.cards = []
    def add_card(self,*ARGS):
        self.cards.append(Card(*ARGS))
    def show_random(self):
        choose = random.choice(self.cards)
        return self.cards[choose]

def test():
    deck = Deck()
    deck.add_card('animal', 'cool thing', 'biology')
    deck.add_card('sdad', 'awesome thing', 'stats')
    pdb.set_trace()
    print deck.show_random().body
test()
