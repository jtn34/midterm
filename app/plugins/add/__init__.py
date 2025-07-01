from app.commands import Command
from decimal import Decimal

class AddCommand(Command):
    def name(self):
        return "add"

    def execute(self, *args):
        if len(args) < 2:
            raise ValueError("Two arguments are required.")

        return args[0] + args[1]