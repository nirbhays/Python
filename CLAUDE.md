# CLAUDE.md — nirbhays/Python

## Repository Purpose

Foundational Python learning exercises built while working through a structured Python curriculum. Covers core language features from conditionals through multi-module projects.

## Owner Context

- **Name:** Nirbhay Singh
- **Background:** Cloud & AI Architect, 11+ years; Python used for scripting, automation, PDF generation, AI agent development
- **Python level in this repo:** Beginner → Intermediate (foundational exercises)

## Repository Structure & Learning Progression

```
Python/
├── Itration/           # Stage 1: Conditionals, types, arithmetic
├── Random and Lists/   # Stage 2: Lists, random module, game logic
├── Loops/              # Stage 3: For/while loops, accumulators
├── Function and Parameters/  # Stage 4: Functions with parameters
├── Funcation with output/    # Stage 5: Return values
├── Dictionary/         # Stage 6: Dicts, nested data structures
├── Global Scope/       # Stage 7: Variable scope, namespacing
├── Hangman/            # Stage 8: Multi-module project
└── BlackJack/          # Stage 9: Card game implementation
```

Note: Folder names contain some typos from the original learning workflow (e.g., "Itration", "Funcation") — preserved as-is to maintain git history.

## Key Files

### Projects (most complete)

**Hangman** — The most complete multi-file project:
- `hangman_main.py` — game loop, imports from other modules
- `hangman_words.py` — word bank list
- `hangman_art.py` — ASCII art for each life stage
- Separate files track the progression of building features incrementally

**BlackJack** (`BlackJack/blackjack-start.py`):
- Card game with dealing, scoring (Ace = 1 or 11), bust logic
- Demonstrates lists, functions, game state

**Caesar Cipher** (`Function and Parameters/Funcations/`):
- `caesar-cipher-1-start.py` — initial version
- `caesar-cipher-final.py` — complete implementation with wrap-around (modulo 26)

**Password Generator** (`Loops/Password Generator Project.py`):
- Generates random passwords from letters + digits + symbols
- Demonstrates random.choice and string building

### Logic Exercises

| File | Concept |
|---|---|
| `Itration/Leap Year.py` | Multi-condition boolean logic |
| `Itration/Treasure Island.py` | Nested if/elif text adventure |
| `Loops/FizzBuzz.py` | Classic FizzBuzz |
| `Dictionary/GRADING PROGRAM.py` | Dict as lookup table |
| `Dictionary/blind-auction-start.py` | Multi-user dict accumulation |
| `Function and Parameters/PRIME NUMBERS.py` | Primality test loop |

## Running Code

```bash
# No dependencies — pure stdlib
python "Hangman/hangman_main.py"
python "BlackJack/blackjack-start.py"
python "Loops/FizzBuzz.py"
python "Function and Parameters/Funcations/caesar-cipher-final.py"
```

Python 3.6+ required. No pip installs needed.

## Code Quality Notes

These are **learning exercises**, not production code. Expect:
- Global variables (scope not always managed)
- Typos in variable names and comments
- Rough/draft files (`rough.py`, `Rough.py`) mixed with final versions
- Incremental builds (start → final pattern for Hangman, Caesar Cipher)

When reviewing or extending this code, treat it as a learning journal rather than a codebase.

## Extending This Repo

Good next exercises to add:
- OOP basics (classes, inheritance)
- File I/O (reading/writing CSV, JSON)
- API calls with `requests`
- Web scraping with `beautifulsoup4`
- Data analysis intro with `pandas`
