# Python Learning Exercises

A collection of foundational Python programming exercises progressing from beginner to intermediate concepts. Built while working through structured Python curriculum covering core language features, logic, and mini-projects.

## Repository Structure

```
Python/
├── Itration/                           # Conditionals, loops, and basic logic
│   ├── first-condition-statement.py    # If/elif/else fundamentals
│   ├── Odd_or_Even.py                  # Modulo and conditional logic
│   ├── Leap Year.py                    # Multi-condition logic
│   ├── BMI Calculator.py               # User input + arithmetic
│   ├── TipCalculator.py                # Float arithmetic
│   ├── Love Calculator.py              # String manipulation + logic
│   ├── Pizza Order Practice.py         # Nested conditionals
│   └── Treasure Island.py             # Text adventure with branching paths
├── Random and Lists/                   # Random module and list operations
│   ├── Random Module.py                # random.randint, random.choice
│   ├── Rock paper scissors.py          # Game logic with randomness
│   ├── Banker Roulette.py             # List indexing and random selection
│   └── Treasure Map.py                # 2D list manipulation
├── Loops/                              # For/while loops and iteration
│   ├── FizzBuzz.py                     # Classic FizzBuzz (for loop)
│   ├── Adding Even Numbers.py          # Range-based loop arithmetic
│   ├── AverageHeight.py                # While loop with accumulator
│   ├── HighScore.py                    # List traversal for max value
│   └── Password Generator Project.py  # Random + string concatenation
├── Function and Parameters/            # Functions with inputs and outputs
│   └── Funcations/
│       ├── Functions with Inputs.py    # def, parameters, arguments
│       ├── Functionwith fixed arguments.py
│       ├── PAINT AREA CALCULATOR.py    # Functions for geometry
│       ├── caesar-cipher-1-start.py    # Caesar cipher introduction
│       ├── caesar-cipher-final.py      # Complete Caesar cipher
│       ├── caeser.py                   # Caesar cipher variant
│       └── art.py                      # ASCII art helper module
│   └── PRIME NUMBERS.py               # Loop + conditional for primality test
├── Funcation with output/              # Return values and function composition
│   ├── calculator-start.py             # Basic calculator with functions
│   ├── DAYS IN MONTH.py               # Return values for calendar logic
│   └── rough.py                        # Scratch/draft work
├── Dictionary/                         # Dictionaries and data structures
│   ├── first dict.py                   # Dictionary basics: create, access, update
│   ├── nested dict.py                  # Nested dictionaries
│   ├── GRADING PROGRAM.py              # Dict lookup for grade mapping
│   ├── blind-auction-start.py          # Dict for multi-user auction
│   └── art.py                          # ASCII art module
├── Global Scope/                       # Variable scope and namespacing
│   ├── Number Gussing Game.py          # Global/local scope in a game
│   └── art.py                          # ASCII art module
└── Hangman/                            # Multi-file project: classic Hangman game
    ├── hangman_main.py                 # Main game loop
    ├── hangman_words.py                # Word bank module
    ├── hangman_art.py                  # ASCII art stages module
    ├── hangman-counting lives.py       # Lives/attempts logic
    ├── Replacing Blanks with Guesses.py # String display logic
    └── Checking if the Player has Won.py # Win condition logic
    └── BlackJack/
        └── blackjack-start.py          # Card game: BlackJack implementation
```

## Concepts Covered

| Topic | Files |
|---|---|
| Variables, types, input | `Itration/` |
| Conditionals (if/elif/else) | `Leap Year.py`, `Treasure Island.py` |
| Lists and indexing | `Random and Lists/` |
| For loops and range | `Loops/FizzBuzz.py`, `Loops/Adding Even Numbers.py` |
| While loops | `Loops/AverageHeight.py` |
| Functions with parameters | `Function and Parameters/` |
| Return values | `Funcation with output/` |
| Dictionaries | `Dictionary/` |
| Nested data structures | `Dictionary/nested dict.py` |
| Variable scope | `Global Scope/` |
| Multi-module projects | `Hangman/` |
| Random module | `Random and Lists/` |
| String manipulation | `caesar-cipher-final.py` |

## Key Projects

### Hangman
Full multi-file Hangman implementation with separate modules for word bank, ASCII art stages, and game logic. Demonstrates modular Python design.

### Caesar Cipher
Classic encryption exercise — shifts each letter by a given amount. Demonstrates string iteration, modular arithmetic, and function design.

### BlackJack
Card game implementation covering game state, list operations, and conditional logic.

### Password Generator
Random character selection from multiple character sets — demonstrates random module and string joining.

## How to Run

```bash
# Any script can be run directly
python "Hangman/hangman_main.py"
python "Loops/FizzBuzz.py"
python "Dictionary/GRADING PROGRAM.py"
```

**Requirements:** Python 3.x (no external libraries needed — stdlib only)

## Learning Path

These exercises follow a structured progression:
1. **Conditionals & basic arithmetic** (Itration)
2. **Lists & randomness** (Random and Lists)
3. **Loops** (Loops)
4. **Functions** (Function and Parameters, Funcation with output)
5. **Dictionaries** (Dictionary)
6. **Scope** (Global Scope)
7. **Multi-module projects** (Hangman, BlackJack)
