from abc import ABCMeta, abstractmethod
import pickle
import json


class SerializationInterface(metaclass=ABCMeta):

    @abstractmethod
    def serialize_data(self):
        pass


class SerializeJSON(SerializationInterface):
    def __init__(self, data):
        self.data = data

    def serialize_data(self):
       with open("json.json", "w") as file:
           json.dump(self.data, file)


class SerializeBinary(SerializationInterface):
    def __init__(self, data):
        self.data = data

    def serialize_data(self):
        with open("binary.bin", "wb") as file:
            pickle.dump(self.data, file)


