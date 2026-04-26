from MovieTicketBooking.Models.Seat import Seat

class SeatService:
    seats: list[Seat]
    seatById: dict[int, Seat]

    def addSeat(self, screenId: int):
        seat = Seat(len(self.seats), screenId)

        self.seats.append(seat)
        self.seatById[seat.id] = seat