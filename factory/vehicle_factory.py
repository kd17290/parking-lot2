from models.vehicle import Vehicle, Car, Truck, SUV, Scooter, Bus, Bike


class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type: str, license_number: str) -> Vehicle:
        match vehicle_type:
            case "car":
                return Car(license_number=license_number)
            case "truck":
                return Truck(license_number=license_number)
            case "suv":
                return SUV(license_number=license_number)
            case "scooter":
                return Scooter(license_number=license_number)
            case "bus":
                return Bus(license_number=license_number)
            case "bike":
                return Bike(license_number=license_number)
            case _:
                raise ValueError(f"Unknown vehicle type: {vehicle_type}")
