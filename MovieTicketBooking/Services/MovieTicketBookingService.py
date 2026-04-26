
from MovieTicketBooking.Models.Screen import Screen
from MovieTicketBooking.Services.MovieAllocationService import MovieAllocationService
from MovieTicketBooking.Services.MovieService import MovieService
from MovieTicketBooking.Services.ScreenService import ScreenService
from MovieTicketBooking.Services.SeatService import SeatService
from MovieTicketBooking.Services.TheaterService import TheaterService


class MovieTicketBookingService:

    def __init__(self):
        self.movieScervice = MovieService()
        self.seatService = SeatService()
        self.screenService = ScreenService(self.seatService)
        self.theaterService = TheaterService(self.screenService)
        self.allocationService = MovieAllocationService()
        pass

    def addMovie(self, name: str):
        self.movieScervice.addMovie(name)
    
    def addTheater(self, name: str, screens: list[list[str]]):
        self.theaterService.addTheather(name, screens)
    
    def addMovieToScreen(self, movieId: int, screenId: int):
        seatIds = self.seatService.getSeats(screenId)

        self.allocationService.allocateSeats(movieId, seatIds)
    
    def bookSeat(self, movieId: int, seatId: int, userId: int):
        self.allocationService.allocateSeatToUser(movieId, seatId, userId)
    
    def printSeatsBookedByUser(self, userId: int):
        seats = self.allocationService.getAllocatedSeatToUser(userId)

        for seat in seats:
            print(seat)

    