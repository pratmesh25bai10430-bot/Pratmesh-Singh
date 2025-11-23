# Rock Paper Scissors Game

A command-line implementation of the classic Rock Paper Scissors game built with Python.

## Overview

This is a simple interactive game where you play Rock Paper Scissors against the computer. The program features a flexible input handler that recognizes partial matches, making gameplay more user-friendly.

## How to Play

1. Run the program
2. Enter your choice when prompted (rock, paper, or scissors)
3. The computer will randomly make its choice
4. The winner is determined based on classic rules:
   - Rock beats Scissors
   - Paper beats Rock
   - Scissors beats Paper
5. Enter '0' to exit the game

## Features

- **Flexible Input**: The input handler can recognize your choice even with typos or partial input
- **Random Computer Opponent**: Computer makes random choices for fair gameplay
- **Continuous Play**: Keep playing rounds until you choose to exit

## Requirements

- Python 3.x
- No external libraries required (uses only built-in `random` module)

## How to Run

```bash
python RockPaperAndScissors.py
```

## Game Rules

```
Rock vs Paper → Paper wins
Paper vs Scissors → Scissors wins
Rock vs Scissors → Rock wins
```

## Example Gameplay

```
Enter '0' to exit
Your choice: rock
Computer's choice: scissors
User Wins !

Your choice: paper
Computer's choice: paper
It's a tie

Your choice: 0
```

## Technical Details

The program uses:
- Dictionary mapping for choice representation
- Pattern matching algorithm for input validation
- Random selection for computer moves
- Conditional logic for win determination

---

**Course**: First Semester Programming Project  
**Language**: Python