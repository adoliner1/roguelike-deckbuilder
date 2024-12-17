from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import random
from enum import Enum

app = FastAPI()

class Direction(str, Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

class CardType(str, Enum):
    MOVE = "move"
    ATTACK = "attack"

class Card(BaseModel):
    id: int
    type: CardType
    name: str
    description: str

class Position(BaseModel):
    x: int
    y: int

class Entity(BaseModel):
    id: int
    position: Position
    hp: int
    max_hp: int

class GameState(BaseModel):
    player: Entity
    enemies: List[Entity]
    grid_size: int = 8
    current_hand: List[Card]
    deck: List[Card]
    discard_pile: List[Card]

# Initialize game state
def create_initial_deck() -> List[Card]:
    deck = []
    for i in range(5):  # 5 move cards
        deck.append(Card(
            id=i,
            type=CardType.MOVE,
            name="Move",
            description="Move up to 1 square in any direction"
        ))
    for i in range(5, 10):  # 5 attack cards
        deck.append(Card(
            id=i,
            type=CardType.ATTACK,
            name="Attack",
            description="Attack an adjacent square"
        ))
    random.shuffle(deck)
    return deck

game_state = None

@app.post("/start-game")
async def start_game():
    global game_state
    deck = create_initial_deck()
    game_state = GameState(
        player=Entity(
            id=0,
            position=Position(x=0, y=0),
            hp=10,
            max_hp=10
        ),
        enemies=[
            Entity(
                id=1,
                position=Position(x=5, y=5),
                hp=5,
                max_hp=5
            )
        ],
        deck=deck,
        current_hand=[],
        discard_pile=[]
    )
    await draw_hand()
    return game_state

@app.post("/play-cards")
async def play_cards(card_indices: List[int]):
    if not game_state:
        raise HTTPException(status_code=400, detail="Game not started")
    
    if len(card_indices) > 3:
        raise HTTPException(status_code=400, detail="Can't play more than 3 cards")
    
    # Play cards
    for idx in card_indices:
        card = game_state.current_hand[idx]
        # Process card effects here
        
    # Enemy turn
    await process_enemy_turn()
    
    # Draw new hand
    await draw_hand()
    return game_state

async def draw_hand():
    if not game_state:
        return
    
    cards_needed = 3 - len(game_state.current_hand)
    
    for _ in range(cards_needed):
        if not game_state.deck:
            # Shuffle discard pile into deck
            game_state.deck = game_state.discard_pile
            game_state.discard_pile = []
            random.shuffle(game_state.deck)
        
        if game_state.deck:
            game_state.current_hand.append(game_state.deck.pop())

async def process_enemy_turn():
    # Simple enemy AI - move towards player if not adjacent, attack if adjacent
    for enemy in game_state.enemies:
        # Process enemy actions here
        pass