from abc import abstractmethod
from dataclasses import dataclass

from models.base_model import BaseModel
from models.parking import (
    ParkingSpotType,
    LargeParkingSpotType,
    SmallParkingSpotType,
    MediumParkingSpotType,
)


@dataclass
class Vehicle(BaseModel):
    license_number: str

    @abstractmethod
    def get_parking_lot_type(self) -> ParkingSpotType:
        ...


@dataclass
class Car(Vehicle):
    def get_parking_lot_type(self) -> ParkingSpotType:
        return MediumParkingSpotType()


@dataclass
class Truck(Vehicle):
    def get_parking_lot_type(self) -> ParkingSpotType:
        return LargeParkingSpotType()


@dataclass
class Bike(Vehicle):
    def get_parking_lot_type(self) -> ParkingSpotType:
        return SmallParkingSpotType()


@dataclass
class SUV(Vehicle):
    def get_parking_lot_type(self) -> ParkingSpotType:
        return MediumParkingSpotType()


@dataclass
class Scooter(Vehicle):
    def get_parking_lot_type(self) -> ParkingSpotType:
        return SmallParkingSpotType()


@dataclass
class Bus(Vehicle):
    def get_parking_lot_type(self) -> ParkingSpotType:
        return LargeParkingSpotType()
