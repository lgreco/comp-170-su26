
number_of_passengers = 12

seats_per_row = 4 

for passenger in range(number_of_passengers):
    seat_label = passenger % seats_per_row
    seat_letter = chr(65 + seat_label)
    row_label = (passenger // seats_per_row) + 1 
    #print("Passenger: ", passenger, "gets to seat", row_label, seat_letter)
    print(f"Passenger {passenger:2d} seats in {row_label}{seat_letter}")
