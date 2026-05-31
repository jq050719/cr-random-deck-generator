import random
from cards import cards
from card import Rarity
from tower_troops import tower_troops

def generate_deck() -> list[str]:
    deck = []
    num_champions = 0

    while len(deck) < 8:
        card = random.choice(cards)

        if card.name in deck:
            continue

        if card.rarity == Rarity.CHAMPION and num_champions == 2:
            continue

        deck.append(card.name)

        if card.rarity == Rarity.CHAMPION:
            num_champions += 1

    tower_troop = random.choice(tower_troops)
    deck.append(tower_troop.name)

    return deck
