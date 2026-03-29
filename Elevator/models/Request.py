from Elevator.enums.DirectionEnum import DirectionEnum
from Elevator.enums.RequestTypeEnum import RequestTypeEnum


class Request:
    type: RequestTypeEnum
    floor: int
    direction: DirectionEnum
    elevatorId: int

    def __init__(self, type: RequestTypeEnum, floor: int, direction: DirectionEnum, eid: int):
        self.type = type
        self.floor = floor
        self.direction = direction
        self.elevatorId = eid