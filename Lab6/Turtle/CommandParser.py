from Commands.ForwardCommand import ForwardCommand
from Commands.LeftCommand import LeftCommand
from Commands.RightCommand import RightCommand

class CommandParser :
    def __init__(self):
        self.mapping = {
            "F":ForwardCommand(),
            "+":RightCommand(),
            "-":LeftCommand(),
        }
    def parse(self,command_string):
        return [self.mapping[c] for c in command_string if c in self.mapping]