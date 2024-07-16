# Game of War Program Requirements

## Overview

Create a Python program to simulate the card game "War" between two players.

## Requirements

### General

- Written in Python
- Executable from the command line

### Deck of Cards

- 52 standard cards (no jokers)
- Each card has a suit (hearts, diamonds, clubs, spades) and rank (2-10, J, Q, K, A)
- Shuffle the deck before starting

### Players

- Two players
- Each player is dealt 26 cards

### Gameplay

- Players reveal the top card from their decks each round
- Higher rank wins the round, takes both cards
- If ranks tie, initiate "war": each player places three cards face down, then one face up
- The higher face-up card wins all the cards
- Repeat until one player has all cards or a set number of rounds

### Winning

- Game ends when one player has all 52 cards or a set round limit is reached
- Player with most cards at the end wins

### User Interaction

- Display results of each round
- Announce the final winner

### Error Handling

- Handle cases where a player can't continue a war due to insufficient cards
- Display appropriate error messages for unexpected inputs or errors

## Optional Features

- Allow multiple games without restarting the program
- Log game outcomes to a file

## Example Output

```
Round 1:
Player 1: 7 of Hearts
Player 2: 5 of Diamonds
Player 1 wins the round.

Press Enter to continue...

Round 2:
Player 1: 3 of Clubs
Player 2: 3 of Spades
War!

Players place three cards face down and one card face up:
Player 1 places face-down cards: (face down), (face down), (face down)
Player 1 places face-up card: King of Hearts
Player 2 places face-down cards: (face down), (face down), (face down)
Player 2 places face-up card: 9 of Diamonds
Player 1 wins the war and takes all the cards.

Press Enter to continue...

```

