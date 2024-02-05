from abc import ABC, abstractmethod


class Faker(ABC):

    @abstractmethod
    def generate_data_by_schema(self, schema: dict) -> dict:
        pass
