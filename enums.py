from typing import Final, Union
from enum import Enum

class Alliance(Enum): 
    RED = 0
    BLUE = 1

class GamePeriod(Enum): 
    AUTONOMOUS = 0
    TELEOP = 1
    ENDGAME = 2

class ParkPosition(Enum): 
    SIGNAL_ZONE = 0
    TERMINAL = 1
    SUBSTATION = 2

class Junction(Enum): 
    GROUND = "G"
    LOW = "L"
    MEDIUM = "M" 
    HIGH = "H"