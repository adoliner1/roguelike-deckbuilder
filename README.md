# Roguelike Deckbuilder

A tactical roguelike deckbuilding game built with Python and FastAPI.

## Setup

1. Create and activate virtual environment:
```bash
# Create venv
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Activate venv (macOS/Linux)
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
cd backend
uvicorn main:app --reload
```

4. Open `frontend/index.html` in your web browser to play the game.

## Game Rules

- Players have a deck of cards consisting of Move and Attack cards
- Play up to 3 cards per turn
- Move cards allow movement in any direction
- Attack cards damage adjacent enemies
- Enemies take their turn after the player
- Goal is to defeat all enemies while staying alive