from MovieTicketBooking.Models.Seat import Seat

class SeatService:
    seats: list[Seat]
    seatById: dict[int, Seat]

    def __init__(self):
        self.seats = []
        self.seatById = {}
        pass

    def addSeat(self, screenId: int):
        seat = Seat(len(self.seats), screenId)

        self.seats.append(seat)
        self.seatById[seat.id] = seat
    
    def getSeats(self, screenId: int):
        seats = []
        
        for seat in self.seats:

            if seat.screenId != screenId:
                continue
            seats.append(seat.id)
        
        return seats