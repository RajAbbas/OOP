from Commands.Command import Command

class RightCommand(Command):
    def execute(self, pen):
        pen.turn_right()