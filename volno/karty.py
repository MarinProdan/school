import random
colors= ("A","B","C","D")
values=("1","2","3","4","5","6","7","8","9","10","J","Q","K")
hnt=0

deck = []

for value in values:
    for color in colors:
      deck.append(color + value)
      
random.shuffle(deck)


print(deck)
print(len(deck), "karet")

card1= deck.pop()
card2= deck.pop()

card1_value = card1[1:]
card2_value = card2[1:]

if card1_value in ("J", "Q", "K"):
    if card1_value == "J":
        card1_value = 10
    elif card1_value == "Q":
        card1_value = 11
    elif card1_value == "K":
        card1_value = 12
if card1_value in range (0,10):
  card1_value=1,2,3,4,5,6,7,8,9,10

if card2_value in ("J", "Q", "K"):
    if card2_value == "J":
        card2_value = 10
    elif card2_value == "Q":
        card2_value = 11
    elif card2_value == "K":
        card2_value = 12
if card2_value in range (0,10):
  card2_value=1,2,3,4,5,6,7,8,9,10



  
print(card1,card1_value)
print(card2,card2_value)
print(deck)
print(len(deck), "karet")

def get_average_deck_value(deck):
    total_value = 0
    for card in deck:
        card_value = int(card[1:]) if card[1:].isdigit() else {"J":10, "Q":11, "K":12}[card[1:]]
        total_value += card_value
    return total_value

# Příklad použití:
average_deck_value = get_average_deck_value(deck)
print(average_deck_value)