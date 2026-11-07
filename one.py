# Vehicle Rental Management System
# PS No. 66

FILE_NAME = "vehicles.txt"


# Class 1: Vehicle
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, model, rental_rate):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.model = model
        self.rental_rate = rental_rate
        self.available = True


# Class 2: Rental
class Rental:
    def __init__(self):
        self.vehicles = []
        self.rentals = {}
        self.load_data()

    # Save data in file
    def save_data(self):
        with open(FILE_NAME, "w") as file:
            for vehicle in self.vehicles:
                vehicle_data = [
                    vehicle.vehicle_id,
                    vehicle.vehicle_type,
                    vehicle.model,
                    str(vehicle.rental_rate),
                    str(vehicle.available)
                ]

                if not vehicle.available:
                    rental_details = self.rentals[vehicle.vehicle_id]
                    vehicle_data += [
                        rental_details[0],
                        str(rental_details[1])
                    ]

                file.write(",".join(vehicle_data) + "\n")

    # Load data from file
    def load_data(self):
        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    vehicle_data = line.strip().split(",")

                    if len(vehicle_data) < 5:
                        continue

                    vehicle = Vehicle(
                        vehicle_data[0],
                        vehicle_data[1],
                        vehicle_data[2],
                        float(vehicle_data[3])
                    )

                    vehicle.available = vehicle_data[4] == "True"
                    self.vehicles.append(vehicle)

                    if not vehicle.available and len(vehicle_data) == 7:
                        self.rentals[vehicle.vehicle_id] = (
                            vehicle_data[5],
                            int(vehicle_data[6])
                        )

        except FileNotFoundError:
            pass

    # Add vehicle
    def add_vehicle(self, vehicle_type, model, rental_rate):
        vehicle_id = "V" + str(len(self.vehicles) + 1)

        vehicle = Vehicle(
            vehicle_id, vehicle_type, model, rental_rate
        )

        self.vehicles.append(vehicle)
        self.save_data()

        print(f"Vehicle added. ID: {vehicle_id} | "
              f"{vehicle_type} | {model} | "
              f"Rs. {rental_rate:g}/day | Available")

    # Find vehicle
    def find_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None

    # Calculate bill
    def calculate_bill(self, rental_rate, rental_days):
        total_bill = rental_rate * rental_days

        if rental_days >= 7:
            total_bill = total_bill * 0.90

        return total_bill

    # Rent vehicle
    def rent_vehicle(self, vehicle_id, customer_name, rental_days):
        vehicle = self.find_vehicle(vehicle_id)

        if vehicle is None:
            print("Vehicle not found.")

        elif not vehicle.available:
            print(f"Vehicle {vehicle_id} is not available.")

        else:
            total_bill = self.calculate_bill(
                vehicle.rental_rate, rental_days
            )

            vehicle.available = False

            self.rentals[vehicle_id] = (
                customer_name, rental_days
            )

            self.save_data()

            message = (
                f"{vehicle_id} rented to {customer_name} "
                f"for {rental_days} days."
            )

            if rental_days >= 7:
                message += " 10% discount applied."

            print(f"{message} Bill: Rs. {total_bill:g}")

    # Return vehicle
    def return_vehicle(self, vehicle_id):
        vehicle = self.find_vehicle(vehicle_id)

        if vehicle is None:
            print("Vehicle not found.")

        elif vehicle.available:
            print(f"Vehicle {vehicle_id} is not rented.")

        else:
            vehicle.available = True
            del self.rentals[vehicle_id]

            self.save_data()

            print(f"{vehicle_id} returned. Status: Available")

    # View available vehicles
    def view_available_vehicles(self):
        vehicle_found = False

        for vehicle in self.vehicles:
            if vehicle.available:
                print(
                    f"{vehicle.vehicle_id} | "
                    f"{vehicle.vehicle_type} | "
                    f"{vehicle.model} | "
                    f"Rs. {vehicle.rental_rate:g}/day | Available"
                )
                vehicle_found = True

        if not vehicle_found:
            print("No vehicles available.")


# Main Program
rental_system = Rental()

while True:
    print("\n===== Vehicle Rental Management System =====")
    print("1. Add Vehicle")
    print("2. Rent Vehicle")
    print("3. Return Vehicle")
    print("4. View Available Vehicles")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        vehicle_type = input("Type: ")
        model = input("Model: ")
        rental_rate = float(input("Rate per day: "))

        rental_system.add_vehicle(
            vehicle_type, model, rental_rate
        )

    elif choice == "2":
        vehicle_id = input("Vehicle ID: ").strip().upper()
        customer_name = input("Customer: ")
        rental_days = int(input("Days: "))

        rental_system.rent_vehicle(
            vehicle_id, customer_name, rental_days
        )

    elif choice == "3":
        vehicle_id = input("Vehicle ID: ").strip().upper()
        rental_system.return_vehicle(vehicle_id)

    elif choice == "4":
        rental_system.view_available_vehicles()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")