from typing import TypeVar, Generic

from singleton import Singleton

T = TypeVar("T")


class InMemoryRepository(Generic[T], metaclass=Singleton):
    def __init__(self):
        self._data: dict[int, T] = {}
        self._counter = 1

    def get(self, key: int) -> T | None:
        return self._data.get(key)

    def create(self, obj: T) -> None:
        obj.id = self._counter
        self._counter += 1
        self._data[obj.id] = obj
        return obj

    def update(self, obj: T) -> None:
        self._data[obj.id] = obj

    def all(self) -> list[T]:
        return list(self._data.values())
