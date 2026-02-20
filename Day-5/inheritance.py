class Device():
    def display(self):
        return "1080p"
    def speaker(self):
        return "sony"
class laptop(Device):
    print("It has Keyboard")
    d1 = Device()
    print(f"The Display Used is {d1.display()}")
    print(f"The Speakers Used is {d1.speaker()}")