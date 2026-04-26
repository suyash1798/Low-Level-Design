Requirements

1. Multiple Theaters
2. Multiple Screens 
3. Generic Seat Map
4. Movie
5. Booking and canel seat
6. Concurency while booking (No two seats booked by same person)

Not in scope

1. Time base booking


Entities

1. MovieTicketBooking
    - TheaterMap
    - Screens
    - MovieToScreen
    - ScreenToTheater
    - getAvailableScreens(movieId)
    - getSeatMap(screenId)
    - book(screenId, seatId, userId) (Syncronised)
    - cancel(bookId)
    - searchMovie(titlePrefix)

2. Theater
    - id
    - name

3. Screen
    - id
    - name
    - theaterId

4. Seat
    - id
    - name
    - screenId
    - available

5. Booking
    - id
    - userId
    - seatId
    - movieId

6. User
    - id
    - name

7. BookingService
    - bookingMap
    - bookTicket(screenId, seat, userId)
    - cancelTicket(bookId)

8, Movie
    - id
    - name


Flow

1. Booking
    - Check for given seatId available or not
    - If available then assign it to user and create a booking

2. Cancel
    - Check if booking Id valid or not
    - If valid then remove it and return true

