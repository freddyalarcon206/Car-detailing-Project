import pricing_module

class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        return f"Customer Name: {self.name}"

class Customer(Person):
    def __init__(self, name, vehicle_type):
        super().__init__(name)
        self.vehicle_type = vehicle_type

    def display_vehicle(self):
        return f"Vehicle Type: {self.vehicle_type}"

class DetailingService:
    def __init__(self, package, add_ons):
        self.package = package
        self.add_ons = add_ons

    def display_services(self):
        return f"Package: {self.package}\nAdd-ons: {', '.join(self.add_ons) if self.add_ons else 'None'}"

    def calculate_cost(self, vehicle_type):
        return pricing_module.calculate_total(self.package, vehicle_type, self.add_ons)

def get_package():
    print("\nAvailable Packages:")
    for key, value in pricing_module.PACKAGE_PRICES.items():
        print(f"{key} - ${value}")

    while True:
        try:
            choice = input("Select a package: ").title()
            if choice not in pricing_module.PACKAGE_PRICES:
                raise ValueError("Invalid package selection.")
            return choice
        except ValueError as e:
            print("Error:", e)

def get_add_ons():
    add_ons = []
    print("\nAvailable Add-ons:")
    for key, value in pricing_module.ADD_ON_PRICES.items():
        print(f"{key} - ${value}")

    print("Type 'done' when finished.")

    while True:
        choice = input("Select add-on: ").title()
        if choice.lower() == "done":
            break
        if choice in pricing_module.ADD_ON_PRICES:
            add_ons.append(choice)
        else:
            print("Invalid add-on.")
    return add_ons

def save_to_file(summary_text):
    try:
        with open("detailing_receipt.txt", "a", encoding="utf-8") as file:
            file.write(summary_text + "\n")
    except IOError:
        print("Error writing to file.")

def main():
    print("Welcome to the Car Detailing Service Program")

    try:
        name = input("Enter customer name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        vehicle_type = input("Enter vehicle type (Sedan, SUV, Truck): ").title()
        if vehicle_type not in ["Sedan", "Suv", "Truck"]:
            raise ValueError("Invalid vehicle type.")

        customer = Customer(name, vehicle_type)

        package = get_package()
        add_ons = get_add_ons()

        service = DetailingService(package, add_ons)

        total_cost = service.calculate_cost(vehicle_type)

        summary = (
            "\n----- SERVICE SUMMARY -----\n"
            + customer.display_name() + "\n"
            + customer.display_vehicle() + "\n"
            + service.display_services() + "\n"
            + f"Total Cost: ${total_cost}\n"
        )

        print(summary)
        save_to_file(summary)

    except ValueError as e:
        print("Input Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)

if __name__ == "__main__":
    main()