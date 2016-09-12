import json


class ModelCollection(object):

    def __init__(self, data):
        self.raw = data
        self.data = data['items']
        self.key_data = None

    def __iter__(self):
        for attr, value in self.data.items():
            yield attr, value

    def __str__(self):
        output = ""
        for attr, value in self:
            output += str(attr) + ": " + str(value) + "\n"
        return output

    def at(self, key=None):
        self.key_data = self.data[key]
        return self

    def get(self, key=None):
        if key is None:
            if self.key_data is None:
                return self.data
            else:
                return self.key_data
        else:
            if self.key_data is None:
                return self.data[key]
            else:
                return self.key_data[key]

    def get_json(self, key=None):
        if key is None:
            if self.key_data is None:
                return json.dumps(self.data)
            else:
                return json.dumps(self.key_data)
        else:
            if self.key_data is None:
                return json.dumps(self.data[key])
            else:
                return json.dumps(self.key_data[key])

    def get_raw(self):
        return self.raw
