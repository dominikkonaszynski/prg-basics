# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    rows = len(seats)
    columns = len(seats[0])
    total_seats = rows * columns
    return total_seats

def seats_available(seats):
    available_count = 0
    for row in seats:
        for seat in row:
            if seat == 'A':
                available_count += 1
    return available_count

def seats_booked(seats): 
   booked_count = 0
   for row in seats:
        for seat in row:
            if seat == 'B':
                booked_count += 1 
   return booked_count

def seat_status(seats, row, place):
    if seats[row-1][place-1] == "A":
        return "This seat is available!"
    elif seats[row-1][place-1] == "B":
        return "This seat is unavailable!"

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats,1,1))
print('Seat in row 5, place 5:', seat_status(cinema_seats,5,5))
print('Seat in row 3, place 5:', seat_status(cinema_seats,3,5))