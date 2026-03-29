from Elevator.enums.DirectionEnum import DirectionEnum
from Elevator.models.Elevator import Elevator


class ElevatorFinder:
    
    @staticmethod
    def getBestAvailableElevator(elevatorsMap: dict[int, Elevator], floor: int, direction: DirectionEnum):
        elevator = None

        for id in elevatorsMap:
            el = elevatorsMap[id]

            if el.direction == direction:
                if direction == DirectionEnum.UP and el.floor < floor:
                    elevator = el
                elif direction == DirectionEnum.DOWN and el.floor > floor:
                    elevator = el
                
                if elevator != None:
                    break
        
        return elevator
