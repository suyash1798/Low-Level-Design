from Elevator.enums.DirectionEnum import DirectionEnum
from Elevator.enums.ElevatorStateEnum import ElevatorStateEnum
import heapq
from typing import Callable


class Elevator:
    id: int
    destinations: set[int]
    maxHeap: list[int]
    minHeap: list[int]
    direction: DirectionEnum | None
    state: ElevatorStateEnum
    floor: int

    observers: list[Callable]

    def __init__(self, id: int):
        self.id = id
        self.state = ElevatorStateEnum.IDLE
        self.destinations = set()
        self.maxHeap = []
        self.minHeap = []
        self.direction = DirectionEnum.UP
        self.floor = 0
        self.observers = []

    def addDestination(self, floor):
        if floor > self.floor:
            self.destinations.add(floor)
            heapq.heappush(self.minHeap, floor)
        elif floor < self.floor:
            self.destinations.add(floor)
            heapq.heappush_max(self.maxHeap, floor)

    def move(self):
        
        if self.state == ElevatorStateEnum.IDLE:
            if len(self.destinations) != 0: 
                if len(self.maxHeap) and self.maxHeap[0] > self.floor:
                    self.notify('directionChange', DirectionEnum.UP)
                    self.direction = DirectionEnum.UP
                    self.state = ElevatorStateEnum.MOVING
                elif len(self.maxHeap) and self.maxHeap[0] < self.floor:
                    self.notify('directionChange', DirectionEnum.DOWN)
                    self.direction = DirectionEnum.DOWN
                    self.state = ElevatorStateEnum.MOVING
        elif len(self.destinations) == 0:
            self.notify('stateChange', ElevatorStateEnum.IDLE)
            self.state = ElevatorStateEnum.IDLE
            self.direction = None
            
        if self.direction == DirectionEnum.UP:
            if len(self.minHeap) and self.floor < self.minHeap[0]:
                self.floor += 1
                if self.floor == self.minHeap[0]:
                    heapq.heappop(self.minHeap)
            elif len(self.maxHeap) and self.floor > self.maxHeap[0]:
                self.floor -= 1
                self.notify('directionChange', DirectionEnum.DOWN)
                self.direction = DirectionEnum.DOWN
                if self.floor == self.maxHeap[0]:
                    heapq.heappop_max(self.maxHeap)
            else:
                self.notify('stateChange', ElevatorStateEnum.IDLE)
                self.state = ElevatorStateEnum.IDLE
                self.direction = None

        elif self.direction == DirectionEnum.DOWN:
            if len(self.maxHeap) and self.floor > self.maxHeap[0]:
                self.floor -= 1
                if self.floor == self.maxHeap[0]:
                    heapq.heappop_max(self.maxHeap)
            elif len(self.minHeap) and self.floor < self.minHeap[0]:
                self.floor += 1
                self.direction = DirectionEnum.UP
                self.notify('directionChange', DirectionEnum.UP)
                if self.floor == self.minHeap[0]:
                    heapq.heappop(self.minHeap)
            else:
                self.notify('stateChange', ElevatorStateEnum.IDLE)
                self.state = ElevatorStateEnum.IDLE
                self.direction = None
        
        if self.floor in self.destinations:
            self.destinations.remove(self.floor)

    def addObserver(self, callback: Callable):
        self.observers.append(callback)
        
    def notify(self, action: str, value: str):
        for ob in self.observers:
            ob(self.id, action, value)