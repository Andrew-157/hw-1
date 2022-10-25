from abc import ABCMeta, abstractmethod
import pickle
import json


class SerializationInterface(metaclass=ABCMeta):

    @abstractmethod
    def serialize_data(self, data):
        pass


class SerializeJSON(SerializationInterface):

    def serialize_data(self, data):
        with open("json.json", "w") as file:
            json.dump(data, file)


class SerializeBinary(SerializationInterface):

    def serialize_data(self, data):
        with open("binary.bin", "wb") as file:
            pickle.dump(data, file)
