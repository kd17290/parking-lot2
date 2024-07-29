from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

from models.base_model import BaseModel


class ParkingSpotStatus(Enum):
    FREE = 0
    OCCUPIED = 1


@dataclass
class ParkingSpotType(BaseModel, ABC):
    @abstractmethod
    def get_hourly_rate(self):
        ...

    @abstractmethod
    def get_size(self):
        ...


@dataclass
class SmallParkingSpotType(ParkingSpotType):
    def get_hourly_rate(self):
        return 10

    def get_size(self):
        return "small"


@dataclass
class MediumParkingSpotType(ParkingSpotType):
    def get_hourly_rate(self):
        return 20

    def get_size(self):
        return "medium"


@dataclass
class LargeParkingSpotType(ParkingSpotType):
    def get_hourly_rate(self):
        return 100

    def get_size(self):
        return "large"


class ParkingGateType(Enum):
    ENTRY = 1
    EXIT = 2


@dataclass
class ParkingLot(BaseModel):
    name: str
    address: str


@dataclass
class ParkingFloor(BaseModel):
    parking_lot: ParkingLot
    floor: int


@dataclass
class ParkingAttendant(BaseModel):
    email: str
    first_name: str
    last_name: str


@dataclass
class ParkingGate(BaseModel):
    parking_lot: ParkingLot
    parking_floor: ParkingFloor
    type: ParkingGateType
    attendant: ParkingAttendant


@dataclass
class ParkingSpot(BaseModel):
    name: str
    parking_floor: ParkingFloor
    parking_lot: ParkingLot
    status: ParkingSpotStatus
    type: ParkingSpotType
