import json
import os


class Storage:
    def __init__(self, filename="inventory.json"):
        self.filename = filename

    def save(self, inventory):
        with open(self.filename, "w") as f:
            json.dump(inventory.to_list(), f, indent=4)

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return json.load(f)