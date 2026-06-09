SEATS = ['A', 'B', 'C']


def assign_seats(num_passengers: int) -> None:
    passenger = 1
    row = 1
    while passenger <= num_passengers:
        for seat in SEATS:
            if passenger > num_passengers:
                break
            print(f"Passenger {passenger:3}  ->  Row {row}, Seat {seat}")
            passenger += 1
        row += 1


def main():
    n = int(input("How many passengers? "))
    assign_seats(n)


if __name__ == "__main__":
    main()
