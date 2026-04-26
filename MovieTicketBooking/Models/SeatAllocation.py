from MovieTicketBooking.Enums.SeatStatus import SeatStatusEnum

class SeatAllocation:
    movieId: int
    seatId: int
    userId: int

    def __init__(self, movieId: int, seatId: int):
        self.movieId = movieId
        self.seatId = seatId
        self.userId = None
