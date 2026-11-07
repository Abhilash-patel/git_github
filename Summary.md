# Project Summary – Vehicle Rental Management System

## 1. Project Overview

The Vehicle Rental Management System is a Python 3 console application developed for **Project Statement No. 66**. It manages vehicle details and basic rental operations.

The program supports adding vehicles, renting vehicles, returning vehicles, viewing available vehicles, calculating bills, and saving/loading information through a text file.

## 2. Main Functions

- **Add Vehicle:** Adds a vehicle and generates its ID.
- **Rent Vehicle:** Checks availability, stores customer/rental details, and calculates the bill.
- **Return Vehicle:** Marks a rented vehicle as available and removes its active rental record.
- **View Available Vehicles:** Displays vehicles that can currently be rented.
- **Save and Load:** Keeps vehicle information in `vehicles.txt` between program runs.

## 3. Data Structures and Concepts

- **Class `Vehicle`:** Holds vehicle ID, type, model, daily rate, and availability.
- **Class `Rental`:** Manages the vehicle list and rental operations.
- **List `self.vehicles`:** Stores all vehicle objects.
- **Dictionary `self.rentals`:** Uses vehicle ID as the key and stores customer name and rental days.
- **File `vehicles.txt`:** Stores vehicle and active rental information.
- **Loops and conditions:** Control the menu, search vehicles, and check availability.

## 4. Bill and Discount Rule

The bill is calculated as:

`Total Bill = Daily Rate × Number of Rental Days`

If the rental period is **7 days or more**, a **10% discount** is applied.

### Examples

| Vehicle | Rate per day | Days | Discount | Final bill |
|---|---:|---:|---:|---:|
| Swift (V1) | Rs. 1500 | 7 | 10% | Rs. 9450 |
| Splendor (V2) | Rs. 500 | 3 | 0% | Rs. 1500 |

## 5. Required Test Cases

Run these tests in the same program session, in the order shown. Start with an empty or backed-up `vehicles.txt` so the first two new vehicles receive IDs V1 and V2.

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

## 6. Test Result Record

The expected outputs above follow the project requirements. Record a test as **PASS** only after running it and checking the actual terminal output.

| Test | Expected result | Actual result |
|---|---|---|
| Test 1 | V1 added and available | To be verified |
| Test 2 | V1 bill is Rs. 9450 | To be verified |
| Test 3 | Already-rented message | To be verified |
| Test 4 | V2 added and available | To be verified |
| Test 4(a) | V2 bill is Rs. 1500 | To be verified |
| Test 4(b) | V2 becomes available | To be verified |

## 7. Test Case Screenshots

Add your **actual successful VS Code terminal screenshots** in this section after running the tests. In GitHub, upload the screenshots in the same repository folder and use Markdown image syntax, for example:

```markdown
![Test Case 1 and 2](test-case-1-2.png)
![Test Case 3 and 4](test-case-3-4.png)
```

**Screenshot note:** The screenshot shared during debugging showed V2 being charged Rs. 4500 instead of the expected Rs. 1500. That screenshot is evidence of the earlier incorrect test run, not a passing result. Replace it with a new screenshot after testing with V2 at Rs. 500 per day.

## 8. Conclusion

This project demonstrates how Python classes, objects, lists, dictionaries, loops, conditional statements, functions, and file handling can be combined to build a simple vehicle rental application.

