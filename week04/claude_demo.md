# Claude Code Demo — Session Transcript

**Course:** COMP 170, Summer 2026  
**Date:** 2026-06-09  
**Working directory:** `week04/`

---

## Prompt 1

> Create a python file called airline.py to assign sequential numbers representing a given number of passengers to a simple seating arrangement of an airplane that has 3 seats row labels A, B, C.

**Claude wrote `week04/airline.py`:**

```python
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
```

**Claude ran the file with 7 passengers to verify:**

```
$ echo "7" | python3 week04/airline.py
How many passengers? Passenger   1  ->  Row 1, Seat A
Passenger   2  ->  Row 1, Seat B
Passenger   3  ->  Row 1, Seat C
Passenger   4  ->  Row 2, Seat A
Passenger   5  ->  Row 2, Seat B
Passenger   6  ->  Row 2, Seat C
Passenger   7  ->  Row 3, Seat A
```

**Claude explained:**

Works correctly. The logic:

- **Outer loop** (`while`) advances the row number after every 3 passengers.
- **Inner loop** (`for seat in SEATS`) cycles through A, B, C within each row.
- The `if passenger > num_passengers: break` handles the last partial row cleanly (e.g., 7 passengers fills rows 1–2 completely and puts one passenger in row 3A).

Run it with `python3 week04/airline.py`.

---

## Prompt 2

> compare the python file you wrote with my code in seat_arrangements.py and discuss the two approaches in the context of a CS1 course

**Claude read both files. This is `seat_arrangements.py`:**

```python
number_of_passengers = 12

seats_per_row = 4 

for passenger in range(number_of_passengers):
    seat_label = passenger % seats_per_row
    seat_letter = chr(65 + seat_label)
    row_label = (passenger // seats_per_row) + 1 
    #print("Passenger: ", passenger, "gets to seat", row_label, seat_letter)
    print(f"Passenger {passenger:2d} seats in {row_label}{seat_letter}")
```

**Claude's comparison:**

---

### Two Approaches to Seat Assignment

#### What each one does

**`seat_arrangements.py`** uses a single `for` loop over `range(number_of_passengers)` and derives the row and seat *mathematically* from the passenger number using integer division (`//`) and modulo (`%`). The seat letter is computed with `chr(65 + seat_label)` — a direct application of what the course covered in week 3 (ASCII codes, `ord`/`chr`).

**`airline.py`** uses a `while` loop wrapping a `for` loop. Row and seat are tracked as *explicit counters* that increment as the loop runs. The seat labels come from a list `['A', 'B', 'C']` rather than from arithmetic.

---

#### For a CS1 course: your approach wins

`seat_arrangements.py` is the stronger teaching artifact for several reasons:

**It reinforces recently taught concepts.** `//` and `%` are workhorses students will use constantly. Seeing them do real work — mapping a flat sequence of numbers onto a 2D grid — builds genuine understanding of why those operators exist.

**The `chr(65 + seat_label)` line is a mini-lesson.** It connects directly to the week 3 ASCII material. Students who memorized that `'A'` is 65 will have a satisfying "aha" moment here.

**It is a single loop.** Nested loops are a significant conceptual jump for beginners. Your flat loop keeps the focus on the math, not on loop structure.

**It is more general.** Change `seats_per_row` from 4 to 6 and it just works — no other change needed. The logic lives entirely in the arithmetic.

---

#### What my version gets wrong for CS1

**Nested loops too early.** The `while`-over-`for` structure is harder to reason about than a single loop with arithmetic. It also requires an `if … break` inside the inner loop to handle the last partial row — that guard is non-obvious and easy to forget.

**The list `['A', 'B', 'C']` hides the structure.** It works, but it obscures the relationship between seat position and seat letter. Students don't see *why* A, B, C — they just see a list.

**The `passenger` counter is manually managed.** Starting at 1 and incrementing inside a nested loop is a classic source of off-by-one errors. Your `range()`-based counter eliminates that category of bug entirely.

---

#### One small note on `seat_arrangements.py`

The passengers are numbered `0` through `11` (because `range(12)` starts at 0). That is probably unintentional — real boarding passes start at 1. Changing line 6 to `range(1, number_of_passengers + 1)` fixes it, though the modulo math on line 7 would then need a small adjustment: `(passenger - 1) % seats_per_row`.

---

**Bottom line:** your flat-loop, math-based approach is pedagogically superior for CS1. It is shorter, more general, directly reuses week 3 material, and avoids the complexity of nested loops. My version was a reasonable general solution but the wrong choice for this course at this point in the semester.
