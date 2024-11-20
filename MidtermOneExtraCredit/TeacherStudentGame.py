from Human import Student, Teacher
from PairGame import Checkers, Chess

student = Student()
teacher = Teacher()

chessGame = Chess()
checkersGame = Checkers()

chessGame.SetPlayerOne(student)
chessGame.SetPlayerTwo(teacher)

checkersGame.SetPlayerOne(student)
checkersGame.SetPlayerTwo(teacher)

chessGame.Play()
checkersGame.Play()