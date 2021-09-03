from Capital.production import Production

production = Production({
    'Resources': [
    ]
})

class Capital():
    def __init__(self, info):
        self.info = info

    def test(self):
        print('seila')

capital = Capital({
    'Production': production
})
