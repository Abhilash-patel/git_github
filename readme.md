# Vehicle Rental Management System

**Project Statement No.:** 66  
**Course:** B.Tech – Computer Science and Engineering  
**Language:** Python 3  
**Application:** Console-based vehicle rental system

## Introduction

The Vehicle Rental Management System is a beginner-friendly Python application for managing vehicles in a rental shop. A user can add vehicles, rent an available vehicle, return a rented vehicle, and view available vehicles.

The program calculates the rental bill automatically. A **10% discount** is applied when a vehicle is rented for **7 days or more**.

## Features

- Add a car, bike, or another vehicle.
- Generate vehicle IDs automatically (V1, V2, V3...).
- Rent an available vehicle to a customer.
- Prevent a vehicle from being rented when it is already rented.
- Return a rented vehicle.
- View all available vehicles.
- Calculate the bill and apply the qualifying discount.
- Save vehicle and active rental details in `vehicles.txt`.
- Load saved data when the program starts.

## Python Concepts Used

| Concept | Use in this project |
|---|---|
| OOP | `Vehicle` and `Rental` classes |
| Objects | Each vehicle is created as a `Vehicle` object |
| Constructor | `__init__()` initializes object data |
| List | `self.vehicles` stores vehicle objects |
| Dictionary | `self.rentals` stores customer and rental-day details using vehicle ID as the key |
| File handling | `load_data()` reads and `save_data()` writes `vehicles.txt` |
| Loops | `while` displays the menu repeatedly; `for` searches and displays vehicles |
| Conditions | `if`, `elif`, and `else` check menu choices and vehicle status |
| Functions/methods | Separate methods perform add, rent, return, search, and billing tasks |

## Project Files

```text
Vehicle-Rental-Management-System/
├── vehicle_rental_management_system.py
├── README.md
├── Summary.md
└── vehicles.txt
```

`vehicles.txt` is created automatically when vehicle data is first saved. It is the program's data file, not the Python source code.

## How to Run

1. Install Python 3.
2. Open this project folder in Visual Studio Code or a terminal.
3. Run:

```bash
python vehicle_rental_management_system.py
```

4. Follow the menu and enter the requested information.

## Main Menu

```text
===== Vehicle Rental Management System =====
1. Add Vehicle
2. Rent Vehicle
3. Return Vehicle
4. View Available Vehicles
5. Exit
```

## Bill Calculation Example

For a Swift car with a rate of Rs. 1500 per day, rented for 7 days:

- Basic amount = 1500 × 7 = Rs. 10500
- Discount = 10% of Rs. 10500 = Rs. 1050
- Final bill = Rs. 9450

For a vehicle rented for 3 days at Rs. 500 per day:

- Final bill = 500 × 3 = Rs. 1500
- No discount applies.

## Test Cases

The expected test sequence and outputs are documented in [Summary.md](Summary.md).

## Note

For a clean first test, back up any existing `vehicles.txt` and start with an empty data file. The program saves data between runs, so previously saved vehicles will remain available when the program is restarted.

