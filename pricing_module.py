PACKAGE_PRICES = {
    "Basic": 50,
    "Standard": 80,
    "Premium": 120
}

ADD_ON_PRICES = {
    "Waxing": 25,
    "Interior Shampoo": 30,
    "Engine Cleaning": 40,
    "Headlight Restoration": 35
}

def vehicle_fee(vehicle_type):
    if vehicle_type.lower() in ["suv", "truck"]:
        return 20
    return 0

def calculate_total(package, vehicle_type, add_ons):
    total = PACKAGE_PRICES.get(package, 0)
    total += vehicle_fee(vehicle_type)
    for item in add_ons:
        total += ADD_ON_PRICES.get(item, 0)
    return total