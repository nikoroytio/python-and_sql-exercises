# ABC = Abstract Base Class
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, sound):
        self.sound = sound
    def makesound(self):
        print(self.sound)

