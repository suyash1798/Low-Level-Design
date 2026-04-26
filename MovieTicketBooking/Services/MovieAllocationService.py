from collections import defaultdict
from MovieTicketBooking.Models.SeatAllocation import SeatAllocation
from MovieTicketBooking.Enums.SeatStatus import SeatStatusEnum

class MovieAllocationService:
    seatAllocations: list[SeatAllocation]
    seatAllocationById: dict[str, SeatAllocation]
    seatAllocationByUserId: dict[int, list]

    def __init__(self):
        self.seatAllocationByUserId = defaultdict(list)
        self.seatAllocationById = {}
        self.seatAllocations = []
        pass

    def allocateSeats(self, movieId: int, seatIds: list[int]):
        for id in seatIds:
            allocation = SeatAllocation(movieId, id)
            self.seatAllocations.append(allocation)
            self.seatAllocationById[(movieId, id)] = allocation
    
    def allocateSeatToUser(self, movieId: int, seatId: int, userId: int) -> bool:
        allocation = self.seatAllocationById[(movieId, seatId)]

        if allocation.userId:
            return False

        allocation.userId = userId
        self.seatAllocationByUserId[userId].append(seatId)

        return True
    
    def getAllocatedSeatToUser(self, userId: int) -> list[int]:
        return self.seatAllocationByUserId[userId]

