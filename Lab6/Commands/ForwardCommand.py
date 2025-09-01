from Commands.Command import Command

class ForwardCommand(Command):
    def execute(self, pen):
        pen.move_forward()