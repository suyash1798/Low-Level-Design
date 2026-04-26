from MovieTicketBooking.Models.Screen import Screen
from MovieTicketBooking.Services.MovieTicketBookingService import MovieTicketBookingService
import threading


movieTicketService = MovieTicketBookingService()

movieTicketService.addMovie('Joker')

screens = [
    ['A', 1, 2, 3, 4, 5],
    ['B', 1, 2, 3, 4, 5]
]

movieTicketService.addTheater('Complex', screens)

for theater in movieTicketService.theaterService.theaters:
    print(theater.id, theater.name)

movieTicketService.addMovieToScreen(0, 1)

for screen in movieTicketService.screenService.screens:
    print(screen.id, screen.name, screen.theaterId)

user1Thread = threading.Thread(target=movieTicketService.bookSeat, args=(0, 5, 0))
user2Thread = threading.Thread(target=movieTicketService.bookSeat, args=(0, 5, 1))

user1Thread.start()
user2Thread.start()

user1Thread.join()
user2Thread.join()

for allocation in movieTicketService.allocationService.seatAllocations:
    print(allocation.movieId, allocation.seatId, allocation.userId)

movieTicketService.printSeatsBookedByUser(0)