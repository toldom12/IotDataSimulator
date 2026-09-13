from abc import ABC, abstractmethod


class DataGenerator(ABC):

    @abstractmethod
    def generate_data(self):
        pass