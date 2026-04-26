from MovieTicketBooking.Models.SeatAllocation import SeatAllocation
from Enums.SeatStatus import SeatStatusEnum

class MovieAllocationService:
    seatAllocations: list[SeatAllocation]
    seatAllocationById: dict[str, SeatAllocation]

    def allocateSeats(movieId: int, seatIds: list[int]):
        for id in seatIds:
            allocation = SeatAllocation(movieId, id)
            self.seatAllocations.append(allocation)
            self.seatAllocationById[(movieId, id)] = allocation
    
    def allocateSeatToUser(movieId: int, seatId: int, userId: int) -> bool:
        allocation = self.seatAllocationById[(movieId, seatId)]

        if allocation.userId:
            return False

        allocation.userId = userId

        return True


