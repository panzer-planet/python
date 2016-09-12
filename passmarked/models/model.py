import json


class Model(object):

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        for attr, value in self.data.items():
            yield attr, value

    def __str__(self):
        output = ""
        for attr, value in self:
            output += str(attr) + ": " + str(value) + "\n"
        return output

    def get(self, key=None):
        if key is None:
            return self.data['item']
        else:
            return self.data['item'][key]

    def get_json(self, key=None):
        if key is None:
            return json.dumps(self.data['item'])
        else:
            return json.dumps(self.data['item'][key])

    def get_raw(self):
        return self.data
