import random
from cards import cards
from tower_troops import tower_troops

def generate_deck() -> list:
    deck = []
    num_champions = 0

    while len(deck) < 8:
        card = random.choice(cards)

        if card.name in deck:
            continue

        if card.rarity == "Champion" and num_champions == 2:
            continue

        deck.append(card.name)

        if card.rarity == "Champion":
            num_champions += 1

    tower_troop = random.choice(tower_troops)
    deck.append(tower_troop.name)

    return deck
