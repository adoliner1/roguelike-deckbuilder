from typing import List
from main import Position, Entity

def is_adjacent(pos1: Position, pos2: Position) -> bool:
    return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y) == 1

def is_valid_move(pos: Position, grid_size: int) -> bool:
    return 0 <= pos.x < grid_size and 0 <= pos.y < grid_size

def get_manhattan_distance(pos1: Position, pos2: Position) -> int:
    return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)