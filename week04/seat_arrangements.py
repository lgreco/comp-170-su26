
number_of_passengers = 12

seats_per_row = 4

# Each passenger is numbered 0, 1, 2, ..., 11.
# We need to turn that single number into a row + seat-letter pair.

for passenger in range(number_of_passengers):

    # % (modulo) gives the remainder after dividing by seats_per_row.
    # That remainder cycles through 0, 1, 2, 3, 0, 1, 2, 3, ...
    # regardless of how many rows there are — perfect for seat position.
    seat_label = passenger % seats_per_row

    # chr(65) == 'A', chr(66) == 'B', etc. (ASCII, as in week 3).
    # Adding seat_label shifts us through A, B, C, D automatically.
    seat_letter = chr(65 + seat_label)

    # // (integer division) discards the remainder and keeps only the quotient.
    # Passengers 0-3 all give quotient 0 (row 0), passengers 4-7 give 1, etc.
    # Adding 1 converts from 0-based counting to the 1-based row numbers
    # passengers expect to see on a ticket.
    row_label = (passenger // seats_per_row) + 1

    #print("Passenger: ", passenger, "gets to seat", row_label, seat_letter)
    # :2d formats the integer with a minimum width of 2, so single-digit
    # passenger numbers align with double-digit ones in the output.
    print(f"Passenger {passenger:2d} seats in {row_label}{seat_letter}")
