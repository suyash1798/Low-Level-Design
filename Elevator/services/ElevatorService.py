from collections import defaultdict
from Elevator.enums.DirectionEnum import DirectionEnum
from Elevator.enums.ElevatorStateEnum import ElevatorStateEnum
from Elevator.enums.RequestTypeEnum import RequestTypeEnum
from Elevator.models.Elevator import Elevator
from Elevator.models.Request import Request
from Elevator.services.ElevatorFinder import ElevatorFinder


class ElevatorService:
    elevatorsMap: dict[int, Elevator] 
    pendingRequests: dict[DirectionEnum, list[Request]]

    def __init__(self, elevators: list[Elevator]):
        self.elevatorsMap = {}
        for elevator in elevators:
            self.elevatorsMap[elevator.id] = elevator
            elevator.addObserver(self.onElevatorAction)

        self.pendingRequests = defaultdict(list)

    def addRequest(self, req: Request):
        if req.type == RequestTypeEnum.IN:
            eId = req.elevatorId
            elevator = self.elevatorsMap[eId]

            elevator.addDestination(req.floor)
        else:
            elevator = ElevatorFinder.getBestAvailableElevator(self.elevatorsMap, req.floor, req.direction)

            if elevator == None:
                self.pendingRequests[req.direction].append(req)
            else:
                elevator.addDestination(req.floor)
    
    def onElevatorAction(self, id: int, action: str, value: str):
        elevator = self.elevatorsMap[id]

        if action == 'stateChange' or action == 'directionChange':
            if value != ElevatorStateEnum.MOVING:
                upreq = self.pendingRequests[DirectionEnum.UP]
                downreq = self.pendingRequests[DirectionEnum.DOWN]

                if len(upreq) != 0:
                    left = []

                    for req in upreq:
                        if req.floor > elevator.floor:
                            elevator.addDestination(req.floor)
                        else:
                            left.append(req)
                    
                    self.pendingRequests[DirectionEnum.UP] = left
                elif len(downreq) != 0:
                    left = []

                    for req in downreq:
                        if req.floor < elevator.floor:
                            elevator.addDestination(req.floor)
                        else:
                            left.append(req)
                    
                    self.pendingRequests[DirectionEnum.DOWN] = left

    
    def move(self):
        for id in self.elevatorsMap:
            el = self.elevatorsMap[id]

            el.move()

            

