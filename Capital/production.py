if __name__ == '__main__':
    from resource import Resource
else:
    from Capital.resource import Resource


import json


class Production():
    def __init__(self):
        self.info = {
            "Resources": [],
            "Supplies": [],
            "Components": [],
            "Buildings": [],
            "Machines": []
            # "Resources": [],
        }
        self.initiate_resources()

    def find_product_category(self, product_name, product_category):
        pass

    def initiate_resources(self):
        with open('Capital/Resources.json') as resources:
            res = json.load(resources)['Resources']
            for resource_info in res:
                Resource(resource_info)

p = Production()
