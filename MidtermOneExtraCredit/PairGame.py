from abc import ABC, abstractmethod
import Human

class PairGame(ABC):
    def __init__(self) -> None:
        self._playerOne = None
        self._playerTwo = None
    
    def SetPlayerOne(self, inputPlayer: Human):
        self._playerOne = inputPlayer

    def SetPlayerTwo(self, inputPlayer: Human):
        self._playerTwo = inputPlayer
    
    @abstractmethod
    def Play(self):
        pass

class Chess(PairGame):
    def Play(self):
        if (self._playerOne and self._playerTwo):
            print(f"The {self._playerOne.GetProfession()} is playing chess against the {self._playerTwo.GetProfession()}.")

class Checkers(PairGame):
    def Play(self):
        if (self._playerOne and self._playerTwo):
            print(f"The {self._playerOne.GetProfession()} is playing checkers against the {self._playerTwo.GetProfession()}.")