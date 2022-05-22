LARGEST_RAND = 100
import random
primitives = ["link", "button", "input-text", "text-area"]

class Element:
    def __init__(self):
        self.elem_type = self.random
        self.url = None

    def set_type(self, elem_type):
        self.elem_type = elem_type

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def get_type(self):
        return self.elem_type

    def random(self):
        self.set_type(random.randint(0,3))

    def __str__(self):
        return "[" + str(primitives[self.elem_type]) + "]"