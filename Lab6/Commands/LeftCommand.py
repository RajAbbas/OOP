from Commands.Command import Command

class LeftCommand(Command):
    def execute(self, pen):
        pen.turn_left()