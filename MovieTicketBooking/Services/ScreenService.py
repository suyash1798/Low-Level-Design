from MovieTicketBooking.Models.Screen import Screen
from MovieTicketBooking.Models.Seat import Seat

class ScreenService:
    screens: list[Screen]
    screenById: dict[int, Screen]

    def addScreen(self, name: str, theaterId: int, seats: list[Seat]):
        screen = Screen(len(self.screens), name, theaterId)

        self.screens.append(screen)
        self.screenById[screen.id] = screen
