from itertools import chain
import time
from functools import lru_cache

with open("11/input.txt", "r") as f:
    stones = tuple([stone for stone in f.read().strip().split(" ")])

@lru_cache(maxsize=None)
def change_stone(stone, blinks):
    if blinks == 0:
        return 1
    
    if stone == "0":
        return change_stone("1", blinks-1)
    elif len(stone) % 2 == 1:
        return change_stone(str(int(stone) * 2024), blinks-1)
    else:
        mid = len(stone) // 2
        left = stone[:mid]
        right = str(int(stone[mid:]))
        return change_stone(left, blinks-1) + change_stone(right, blinks-1)

    
def change_stones(stones: list[int], blinks: int) -> list[int]:
    numb_stones = 0
    for stone in stones:
        numb_stones += change_stone(stone, blinks)
    return numb_stones

for blinks in [25, 75]:
    print(f"Nº Stones after {blinks} blinks: {change_stones(stones, blinks)}")
