"""
Vehicle Rental Management System (PS No. 66)
Language : Python 3
Concepts : OOP, Lists, Dictionaries, File Handling
"""

FILE_NAME = "vehicles.txt"
DISCOUNT_DAYS = 7        # itne ya zyada din par discount milega
DISCOUNT_PERCENT = 10    # discount percentage


def show_amount(amount):
    """1500.0 ko 1500 dikhata hai, 9450.5 ko 9450.5 hi rehne deta hai."""
    if amount == int(amount):
        return str(int(amount))
    return str(amount)


# ---------------------------------------------------------------
# CLASS 1: Vehicle -> ek vehicle ki saari details rakhti hai
# ---------------------------------------------------------------
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, model, rate, available=True):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.model = model
        self.rate = rate            # rate per day
        self.available = available  # True = Available, False = Rented

    def status(self):
        return "Available" if self.available else "Rented"

    def details(self):
        return (f"ID: {self.vehicle_id} | {self.vehicle_type} | {self.model} | "
                f"Rs. {show_amount(self.rate)}/day | {self.status()}")


# ---------------------------------------------------------------
# CLASS 2: Rental -> vehicles ka list + rental dictionary manage karti hai
# ---------------------------------------------------------------
class Rental:
    def __init__(self):
        self.vehicles = []   # LIST: saare Vehicle objects
        self.rentals = {}    # DICTIONARY: vehicle_id -> {"customer", "days", "bill"}
        self.load_from_file()

    # ---------- File Handling ----------
    def save_to_file(self):
        """Har line: id,type,model,rate,status,customer,days"""
        with open(FILE_NAME, "w") as file:
            for v in self.vehicles:
                line = [v.vehicle_id, v.vehicle_type, v.model,
                        str(v.rate), v.status()]
                if not v.available:
                    info = self.rentals[v.vehicle_id]
                    line.append(info["customer"])
                    line.append(str(info["days"]))
                file.write(",".join(line) + "\n")

    def load_from_file(self):
        """Program start hote hi file se data wapas load karta hai."""
        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) < 5:
                        continue  # kharab/khali line skip
                    vehicle_id, vehicle_type, model, rate, status = parts[:5]
                    vehicle = Vehicle(vehicle_id, vehicle_type, model,
                                      float(rate), status == "Available")
                    self.vehicles.append(vehicle)
                    if status == "Rented" and len(parts) == 7:
                        days = int(parts[6])
                        bill = self.calculate_bill(vehicle.rate, days)
                        self.rentals[vehicle_id] = {"customer": parts[5],
                                                    "days": days,
                                                    "bill": bill}
        except FileNotFoundError:
            pass  # pehli baar run ho raha hai, file abhi nahi bani

    # ---------- Helper functions ----------
    def find_vehicle(self, vehicle_id):
        """List me loop chala ke vehicle dhoondta hai."""
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                return v
        return None

    def generate_id(self):
        """Naya ID: V1, V2, V3 ... (V1 se start)"""
        highest = 0
        for v in self.vehicles:
            digits = v.vehicle_id[1:]
            if digits.isdigit():          # sirf sahi ID (V1, V2...) count karo
                number = int(digits)
                if number > highest:
                    highest = number
        return "V" + str(highest + 1)

    def calculate_bill(self, rate, days):
        """Bill = rate x days; 7 ya zyada din par 10% discount."""
        bill = rate * days
        if days >= DISCOUNT_DAYS:
            bill = bill - bill * DISCOUNT_PERCENT / 100
        return bill

    # ---------- Main features ----------
    def add_vehicle(self, vehicle_type, model, rate):
        vehicle = Vehicle(self.generate_id(), vehicle_type, model, rate)
        self.vehicles.append(vehicle)
        self.save_to_file()
        print("Vehicle added.", vehicle.details())

    def rent_vehicle(self, vehicle_id, customer, days):
        vehicle = self.find_vehicle(vehicle_id)
        if vehicle is None:
            print(f"Vehicle {vehicle_id} not found.")
            return
        if not vehicle.available:
            print(f"Vehicle {vehicle_id} is not available.")
            return

        bill = self.calculate_bill(vehicle.rate, days)
        vehicle.available = False
        self.rentals[vehicle_id] = {"customer": customer,
                                    "days": days,
                                    "bill": bill}
        self.save_to_file()

        message = f"{vehicle_id} rented to {customer} for {days} days."
        if days >= DISCOUNT_DAYS:
            message += f" {DISCOUNT_PERCENT}% discount applied."
        message += f" Bill: Rs. {show_amount(bill)}"
        print(message)

    def return_vehicle(self, vehicle_id):
        vehicle = self.find_vehicle(vehicle_id)
        if vehicle is None:
            print(f"Vehicle {vehicle_id} not found.")
            return
        if vehicle.available:
            print(f"Vehicle {vehicle_id} is not rented.")
            return

        vehicle.available = True
        del self.rentals[vehicle_id]   # dictionary se rental details hata do
        self.save_to_file()
        print(f"{vehicle_id} returned. Status: {vehicle.status()}")

    def view_available(self):
        print("Available vehicles:")
        found = False
        for v in self.vehicles:
            if v.available:
                print(" ", v.details())
                found = True
        if not found:
            print("  No vehicles available.")


# ---------------------------------------------------------------
# Input lene ke safe functions (galat input par crash nahi hoga)
# ---------------------------------------------------------------
def read_number(message, number_type, minimum):
    """Jab tak sahi number na mile, tab tak poochta rehta hai."""
    while True:
        try:
            value = number_type(input(message))
            if value < minimum:
                print(f"Value must be {minimum} or more.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_menu():
    print("\n===== Vehicle Rental Management System =====")
    print("1. Add vehicle")
    print("2. Rent vehicle")
    print("3. Return vehicle")
    print("4. View available vehicles")
    print("5. Exit")


def main():
    shop = Rental()
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            vehicle_type = input("Type: ").strip()
            model = input("Model: ").strip()
            rate = read_number("Rate per day: ", float, 1)
            shop.add_vehicle(vehicle_type, model, rate)

        elif choice == "2":
            vehicle_id = input("Vehicle ID: ").strip().upper()
            customer = input("Customer: ").strip()
            days = read_number("Days: ", int, 1)
            shop.rent_vehicle(vehicle_id, customer, days)

        elif choice == "3":
            vehicle_id = input("Vehicle ID: ").strip().upper()
            shop.return_vehicle(vehicle_id)

        elif choice == "4":
            shop.view_available()

        elif choice == "5":
            print("Thank you! Data saved in", FILE_NAME)
            break

        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()