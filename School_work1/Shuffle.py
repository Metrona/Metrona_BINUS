#%%
from random import shuffle

def Cards():
    suits = ["heart", "spade", "diamond", "club"]
    values = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards = ""
    for x in suits:
        for y in values:
            cards += (x + " " + y + "\n")
    cards = cards.split("\n")
    shuffle (cards)
    print (cards)
Cards()