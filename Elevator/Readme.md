Requirements

1. Able to request a floor from outside
2. Able to select a floor from inside
3. Support multiple elevator
4. Assign best available elevator for every request. Nearest with same distance


Entities

1. Elevator
    - id
    - destination floor
    - direction (UP, DOWN)
    - state (idle, moving, open)
    - addDestination(floor)
    - move()
    - notify() // used for state & direction change
2. Request
    - type (OUT, IN)
    - ElevatorId
    - floor
    - direction (UP, DOWN) // Only in case of OUT request
3. ElevatorStateEnum
    - IDLE
    - MOVING
    - Open
4. RequestTypeEnum
    - IN
    - OUT
5. DirectionEnum
    - UP
    - DOWN
6. ElevatorFinder
    - getBestAvailableElevator(floor, Direction)
7. ElevatorSystem
    - elevators
    - pendingRequests
    - request(request)
    - listner() // state & direction change

FLow

1. Out Request

    - User request a elevator from outside
    - ElevatorFinder will search for elevator with same direction and not crossed req floor
    - In those elevator, elevator with minimum distance will be assigned
    - If no elevator found it insert into pending requests
    - On every elevator move, Elevator system will be notfied and try to assign pending requests

2. In Request
    
    - If floor not available then request will be rejected
    - Floor will directly inserted into the same elevator unique set
    - In request with a valid floor needs to be server by same elevator but with least priority