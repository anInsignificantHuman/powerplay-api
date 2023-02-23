import re
from enums import * 
from errors import * 
from typing import Optional

junctions = [
    ["G", "L", "G", "L", "G"], 
    ["L", "M", "H", "M", "L"], 
    ["G", "H", "G", "H", "G"], 
    ["L", "M", "H", "M", "L"], 
    ["G", "L", "G", "L", "G"]
]

def get_coords(coordinate: str): 
    char = coordinate[0]
    num = int(coordinate[1])
    return 5 - num, ord(char) - ord('V')

class Field: 
    score = [0, 0]
    period = GamePeriod.AUTONOMOUS
    junction_scores = [[0 for _ in range(5)] for _ in range(5)]

    def set_period(self, period: GamePeriod): 
        self.period = period

    def increment_score(self, alliance: Alliance, value: int): 
        self.score[alliance.value] += value
    
class Robot: 
    def __init__(self, field: Field, alliance: Alliance): 
        self.field = field 
        self.alliance = alliance
    
    def park(self, position: ParkPosition, custom_sleeve = False): 
        if (self.field.period == GamePeriod.TELEOP):
            raise SequenceError(self.park, self.field.period)
        
        elif (position == ParkPosition.TERMINAL): 
            self.field.increment_score(self.alliance, 2)

        elif (self.field.period == GamePeriod.AUTONOMOUS): 
            value = 10 * (custom_sleeve + 1) if position == ParkPosition.SIGNAL_ZONE else 2
            self.field.increment_score(self.alliance, value)
        

    def score(self, coordinate: str):
        coordinate = coordinate.upper() 
        if (not (len(coordinate) == 2 and re.match(r"[V-Z][1-5]", coordinate))): 
            raise CoordinateError(coordinate)
        
        xCoord, yCoord = get_coords(coordinate)
        junction = Junction(junctions[xCoord][yCoord])

        if (self.field.period == GamePeriod.AUTONOMOUS): 
            pass
        elif (self.field.period == GamePeriod.TELEOP): 
            pass
        elif (self.field.period == GamePeriod.ENDGAME): 
            pass

field1 = Field()
bot = Robot(field1, Alliance.BLUE)
bot.score("X3")
