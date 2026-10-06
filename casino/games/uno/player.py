import random
from casino.cards import UnoCard
from casino.utils import cprint

class Player:
    def __init__(self, id, name) :
        self.id = id
        self.name = name.upper()
        self.hand = []
        # The below integers will keep track of how many draws a player has performed and how many cards played overall.
        # Acutally, keeping track of the number of draws/cards doesn't really matter since both numbers will always be the same.
        self.draws = 0
        # The below integers will keep track of what kind of cards each player played, from the standard uno card types.
        # The properity of what kinda of card is played is defined as a string: "rank" in cards.py
        self.plus2_cards = 0
        self.plus4_cards = 0
        self.reverse_cards = 0
        self.skip_cards = 0
        self.wild_cards = 0
    
    def draw(self, deck: list[UnoCard]) -> UnoCard:
        c = random.choice(deck)
        self.hand.append(c)
        # Add 1 to the draw stat stored in each player.
        self.draws += 1
        deck.remove(c)
        return c
    
    # I can't say I understand what this function does, despite the name.
    # Additionally, this function is defined here but never used anywhere.
    def play_card(self) -> UnoCard:
        c = random.choice(self.hand)
        self.hand.remove(c)
        return c
    
    def playable_cards(self, currentCard : UnoCard) -> list[UnoCard]:
        valid_cards = []
        for i in self.hand : 
            if (i.rank == currentCard.rank or i.color == currentCard.color or i.color == "wild") :
                valid_cards.append(i)
        return valid_cards