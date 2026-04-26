from MovieTicketBooking.Models.Screen import Screen
from MovieTicketBooking.Models.Seat import Seat
from MovieTicketBooking.Services.SeatService import SeatService

class ScreenService:
    screens: list[Screen]
    screenById: dict[int, Screen]

    def __init__(self, seatService: SeatService):
        self.screens = []
        self.screenById = {}
        self.seatService = seatService
        pass

    def addScreen(self, name: str, theaterId: int, seats: list[Seat]):
        screen = Screen(len(self.screens), name, theaterId)

        self.screens.append(screen)
        self.screenById[screen.id] = screen

        for seat in seats:
            self.seatService.addSeat(screen.id)

