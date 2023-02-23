from enums import *
from typing import Callable

class SequenceError(Exception): 
    def __init__(self, function: Callable, period: GamePeriod): 
        super().__init__(f".{function.__name__}() cannot be called during {period.name.lower()}")

class CoordinateError(Exception): 
    def __init__(self, coordinate: str): 
        super().__init__(f"Invalid coordinate '{coordinate}'")

def hi(): 
    return 'hi'