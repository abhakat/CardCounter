import random

class blackjackDeck:
    basicDeck = [
    "A of Hearts", "2 of Hearts", "3 of Hearts", 
    "4 of Hearts", "5 of Hearts", "6 of Hearts", 
    "7 of Hearts", "8 of Hearts", "9 of Hearts",
    "10 of Hearts", "J of Hearts", "Q of Hearts",
    "K of Hearts",
    "A of Clubs", "2 of Clubs", "3 of Clubs",
    "4 of Clubs", "5 of Clubs", "6 of Clubs", 
    "7 of Clubs", "8 of Clubs", "9 of Clubs", 
    "10 of Clubs", "J of Clubs", "Q of Clubs",
    "K of Clubs", 
    "A of Diamonds", "2 of Diamonds", "3 of Diamonds", 
    "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", 
    "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", 
    "10 of Diamonds", "J of Diamonds", "Q of Diamonds", 
    "K of Diamonds", 
    "A of Spades", "2 of Spades", "3 of Spades", 
    "4 of Spades","5 of Spades", "6 of Spades", 
    "7 of Spades", "8 of Spades", "9 of Spades", 
    "10 of Spades", "J of Spades", "Q of Spades", 
    "K of Spades"
    ]
    # Hi-Lo system count map
    count_map = {
        "2": 1, "3": 1, "4": 1, "5": 1, "6": 1,
        "7": 0, "8": 0, "9": 0,
        "10": -1, "J": -1, "Q": -1, "K": -1, "A": -1
    }


    def __init__(self, numberOfDecks):
        self.gameDeck = []
        self.runningCount = 0
        for i in range(numberOfDecks):
            self.gameDeck.extend((self.basicDeck).copy())
        
        self.cardCount = len(self.gameDeck)
        random.shuffle(self.gameDeck)
        print(self.gameDeck)

    def drawCard(self):
        currCard =  self.gameDeck.pop()
        self.update_running_count(currCard)
        return currCard
    
    def get_cards_left(self):
        return len(self.gameDeck)
    
    def update_running_count(self, inputCard):
        first_part, second_part = inputCard.split(' ', 1)
        rcVal = self.count_map[first_part]
        self.runningCount += rcVal

    def get_running_count(self):
        return self.runningCount

    def trueCount(self):
        #decks remaining
        decksRemaining = (self.get_cards_left()) / 52
        return (self.get_running_count() // decksRemaining)
    


    
    
    
    



# player_deck = blackjackDeck(3)
# for i in range(25):
#     print(player_deck.drawCard())

# print(player_deck.trueCount())



