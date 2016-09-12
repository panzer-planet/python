import json


class Error(object):

    def __init__(self, data):
        self.raw = data
        self.code = data['code']
        self.status = data['status']
        self.message = data['message']

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __str__(self):
        output = ""
        for attr, value in self:
            output += str(attr) + ": " + str(value) + "\n"
        return output

    def at(self):
        return self

    def get(self):
        return self

    def to_json(self):
        return json.dumps(self.__dict__)

    def get_raw(self):
        return self.raw
