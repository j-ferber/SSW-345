from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self):
        self._SetProfession()
    
    @abstractmethod
    def _SetProfession(self):
        pass
    
    def GetProfession(self):
        return self._profession
    
class Student(Human):
    def _SetProfession(self):
        self._profession = "student"
    
class Teacher(Human):
    def _SetProfession(self):
        self._profession = "teacher"