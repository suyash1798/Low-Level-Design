import random
from Elevator.enums.DirectionEnum import DirectionEnum
from Elevator.enums.RequestTypeEnum import RequestTypeEnum
from Elevator.models.Elevator import Elevator
from Elevator.models.Request import Request
from Elevator.services.ElevatorService import ElevatorService


elevators = []

for i in range(1, 6):
    el = Elevator(i)
    elevators.append(el)

requests = []

for i in range(1, 20):
    rq = Request(RequestTypeEnum.IN, random.randint(1,50), DirectionEnum.UP, random.randint(1, 5))
    requests.append(rq)

    rq = Request(RequestTypeEnum.OUT, random.randint(1,50), DirectionEnum.UP, random.randint(1, 5))
    requests.append(rq)

    rq = Request(RequestTypeEnum.IN, random.randint(1,50), DirectionEnum.DOWN, random.randint(1, 5))
    requests.append(rq)

    rq = Request(RequestTypeEnum.OUT, random.randint(1,50), DirectionEnum.DOWN, random.randint(1, 5))
    requests.append(rq)

random.shuffle(requests)

elevatorService = ElevatorService(elevators)

while len(requests) != 0:
    if random.randint(1,2) == 1:
        rq = requests.pop()
        elevatorService.addRequest(rq)
        print("New Request\n")
    else:
        elevatorService.move()
        print("Elevators moving ... \n")
    
    for id in elevatorService.elevatorsMap:
        elevator = elevatorService.elevatorsMap[id]

        print(str(elevator.floor) + " ")
    
    print("\n")