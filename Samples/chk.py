class Box:
    def __init__(self, volume):
        self.volume = volume

    def __add__(self, other):
        return Box(self.volume + other.volume)

    def __str__(self):
        return f"Volume: {self.volume}"

b1 = Box(10)
b2 = Box(20)
b3 = b1 + b2  # Calls __add__()
print(b3)

