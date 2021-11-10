import TestData
import json


class Utility:
    @staticmethod
    def rear_json(file):
        with open(file, 'r') as f:
            read_json = json.load(f)
        return read_json



