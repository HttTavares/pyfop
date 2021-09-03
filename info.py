class Info():
    def __init__(self, json):
        # self.
        # for key in list( json.keys() ):
            # print(key)
            # self.
        self._json = json

    @property
    def json(self, info_name):
        return self._json[info_name]

    # @property
    # def json(self):
    #     return self._json

    # @scalar.setter
    # def scalar(self, value):
    #     self._scalar = value

if __name__ == '__main__':
    info = Info({
        'Seila': 10,
        'Outro': 'a'
    })
    print(info.json('Seila'))
