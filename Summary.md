# Project Summary – Vehicle Rental Management System

## 1. Project Overview

The Vehicle Rental Management System is a Python 3 console application developed for **Project Statement No. 66**. It helps a rental shop manage vehicles and their rental status.

The program allows the user to add vehicles, rent available vehicles, return rented vehicles, view available vehicles, calculate bills, and save/load information using a text file.

A **10% discount** is applied when a vehicle is rented for **7 days or more**.

## 2. How I Created the Project

I developed this project step by step using Python:

1. I first identified the main operations required: add, rent, return, and view vehicles.
2. I created a `Vehicle` class to store each vehicle's ID, type, model, daily rate, and availability.
3. I created a `Rental` class to manage the vehicle list and rental operations.
4. I used a list to store vehicle objects and a dictionary to store active rental details.
5. I created separate methods for adding vehicles, finding vehicles, calculating bills, renting, returning, and viewing vehicles.
6. I used file handling to save information in `vehicles.txt` and load it when the program starts.
7. Finally, I tested the program using the test cases given in the project statement.

## 3. Project Features

- Add a car, bike, or another vehicle.
- Generate vehicle IDs automatically (V1, V2, V3...).
- Rent an available vehicle to a customer.
- Prevent a vehicle from being rented when it is already rented.
- Return a rented vehicle.
- View all available vehicles.
- Calculate rental bills automatically.
- Apply a 10% discount for rentals of 7 days or more.
- Save vehicle and active rental details in `vehicles.txt`.
- Load saved data when the program starts.

## 4. Python Concepts Used

| Concept | Use in this project |
|---|---|
| OOP | `Vehicle` and `Rental` classes |
| Objects | Each vehicle is created as a `Vehicle` object |
| Constructor | `__init__()` initializes object data |
| List | `self.vehicles` stores vehicle objects |
| Dictionary | `self.rentals` stores customer name and rental days using vehicle ID as the key |
| File handling | `load_data()` reads and `save_data()` writes `vehicles.txt` |
| Loops | `while` displays the menu repeatedly; `for` searches and displays vehicles |
| Conditions | `if`, `elif`, and `else` check menu choices and vehicle status |
| Functions/methods | Separate methods perform add, rent, return, search, and billing tasks |

## 5. Bill and Discount Rule

The bill is calculated as:

`Total Bill = Daily Rate × Number of Rental Days`

If the rental period is **7 days or more**, a **10% discount** is applied.

### Examples

| Vehicle | Rate per day | Days | Discount | Final bill |
|---|---:|---:|---:|---:|
| Swift (V1) | Rs. 1500 | 7 | 10% | Rs. 9450 |
| Splendor (V2) | Rs. 500 | 3 | 0% | Rs. 1500 |

## 6. Challenges Faced and How I Solved Them

The following are suitable project-report points. Keep only the points that match what you actually experienced while developing and testing your program.

### Challenge 1: Generating unique vehicle IDs
**Problem:** I needed to make sure every newly added vehicle received a different ID.

**Solution:** I used a vehicle ID generation method that checks the existing IDs and creates the next ID, such as V1, V2, and V3.

### Challenge 2: Checking vehicle availability
**Problem:** The program should not allow a customer to rent a vehicle that is already rented.

**Solution:** I used the vehicle's `available` status and conditional statements to check whether the vehicle can be rented.

### Challenge 3: Calculating the rental bill
**Problem:** The bill needed to include a 10% discount for rentals of 7 days or more.

**Solution:** I created a separate `calculate_bill()` method to calculate the amount and apply the discount when the condition is met.

### Challenge 4: Saving data permanently
**Problem:** Vehicle information should remain available even after closing and reopening the program.

**Solution:** I used file handling with `vehicles.txt`. The `save_data()` method writes the data, and `load_data()` reads it when the program starts.

### Challenge 5: Testing vehicle records
**Problem:** During testing, I encountered a case where the vehicle ID or saved rate did not match the expected test data.

**Solution:** I checked the vehicle records in `vehicles.txt`, verified the ID and daily rate, and repeated the test with the correct starting data.

## 7. Required Test Cases

Run these tests in the same program session, in the order shown. For a clean test, back up or clear the existing `vehicles.txt` first so the new vehicles receive IDs V1 and V2.

### Test Case 1 – Normal Input: Add a vehicle

Enter each value when prompted:

```text
1
Car
Swift
1500
```

Expected result:

```text
Vehicle added. ID: V1 | Car | Swift | Rs. 1500/day | Available
```

### Test Case 2 – Boundary Input: Rent for 7 days

```text
2
V1
Aman
7
```

Expected result:

```text
V1 rented to Aman for 7 days. 10% discount applied. Bill: Rs. 9450
```

### Test Case 3 – Invalid Operation: Rent an already rented vehicle

```text
2
V1
Riya
2
```

Expected result:

```text
Vehicle V1 is not available.
```

### Test Case 4 – Different Valid Scenario: Add a bike

```text
1
Bike
Splendor
500
```

Expected result:

```text
Vehicle added. ID: V2 | Bike | Splendor | Rs. 500/day | Available
```

### Test Case 4(a) – Rent the bike for 3 days

```text
2
V2
Neha
3
```

Expected result:

```text
V2 rented to Neha for 3 days. Bill: Rs. 1500
```

### Test Case 4(b) – Return the bike

```text
3
V2
```

Expected result:

```text
V2 returned. Status: Available
```

## 8. Test Result Record

The expected outputs above follow the project requirements. Mark a test as **PASS** only after running it and checking the actual terminal output.

| Test | Expected result | Actual result |
|---|---|---|
| Test 1 | V1 added and available | To be verified |
| Test 2 | V1 bill is Rs. 9450 | To be verified |
| Test 3 | Already-rented message | To be verified |
| Test 4 | V2 added and available | To be verified |
| Test 4(a) | V2 bill is Rs. 1500 | To be verified |
| Test 4(b) | V2 becomes available | To be verified |

## 9. Test Case Screenshots
<img width="840" height="307" alt="Screenshot 2026-11-07 130724" src="https://github.com/user-attachments/assets/e25ac264-4d4d-4ab3-b9fd-44ba5a02507a" />
<img width="797" height="280" alt="Screenshot 2026-11-07 130822" src="https://github.com/user-attachments/assets/81b1abc0-e850-4bed-9d4c-6f605e62a1a8" />
<img width="651" height="285" alt="Screenshot 2026-11-07 131017" src="https://github.com/user-attachments/assets/20b0cb6b-832f-4813-8ab4-27b6781993a5" />
<img width="687" height="320" alt="Screenshot 2026-11-07 131225" src="https://github.com/user-attachments/assets/caf411cf-d4cf-44a8-9ced-ac7472697eb4" />

<img width="675" height="257" alt="Screenshot 2026-11-07 131306" src="https://github.com/user-attachments/assets/1e3de7f3-b148-43f1-a44f-a8f5a34019ee" />
## 10. Questions and Answers

### Q1. What is the main purpose of this project?
**Answer:** The main purpose is to manage vehicle rentals, including adding vehicles, renting them, returning them, and viewing available vehicles.

### Q2. How did you create this project?
**Answer:** I created it using Python 3. I divided the work into two classes, `Vehicle` and `Rental`, and used methods for different operations. I used a list for vehicle objects, a dictionary for rental details, and file handling to save and load data.

### Q3. Which programming language did you use?
**Answer:** I used Python 3.

### Q4. Where did you use OOP?
**Answer:** I used OOP by creating two classes: `Vehicle` and `Rental`. I used objects, a constructor, attributes, and methods.

### Q5. Where did you use a list?
**Answer:** I used `self.vehicles` to store all the vehicle objects.

### Q6. Where did you use a dictionary?
**Answer:** I used `self.rentals` to store rental information. The vehicle ID is used as the key, and customer name and rental days are stored as the value.

### Q7. Where did you use file handling?
**Answer:** I used `save_data()` to write information to `vehicles.txt` and `load_data()` to read saved information when the program starts.

### Q8. Which loops did you use?
**Answer:** I used a `while` loop to keep showing the menu until the user exits. I used `for` loops to search through vehicles, display them, and read file lines.

### Q9. How is the rental bill calculated?
**Answer:** The daily rental rate is multiplied by the number of rental days. If the rental period is 7 days or more, a 10% discount is applied.

### Q10. How does the program prevent double renting?
**Answer:** Before renting, the program checks the vehicle's availability. If it is already rented, the program displays a message and does not rent it again.

### Q11. What happens when the program is restarted?
**Answer:** The program loads the saved vehicle and active rental information from `vehicles.txt`.

### Q12. What difficulties did you face while making this project?
**Answer:** I faced challenges in generating unique vehicle IDs, checking vehicle availability, calculating the discount correctly, and saving and loading data using file handling. I solved these by creating separate methods and testing each operation.

### Q13. What did you learn from this project?
**Answer:** I learned how to use classes and objects, lists, dictionaries, loops, functions, conditional statements, and file handling together in a practical Python project.

### Q14. What improvements can be added in the future?
**Answer:** In the future, the project can include a graphical user interface, customer records, search options, rental history, and database connectivity.

## 11. Conclusion

This project demonstrates how Python classes, objects, lists, dictionaries, loops, conditional statements, functions, and file handling can be combined to build a simple vehicle rental application. It also helped me understand how to divide a problem into smaller functions and test a program using different inputs.
