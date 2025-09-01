from Turtle.CommandParser import CommandParser
from Turtle.Turtle import Turtle


turtle = Turtle()
parser = CommandParser()

#square
command1 = parser.parse("F+F+F+F+F-")
turtle.run(command1)

#zigzag
command2 = parser.parse("F-F+F-F")
turtle.run(command2)
