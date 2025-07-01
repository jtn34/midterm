from app.commands import Command
from decimal import Decimal
from calculator.operations import subtract

class SubtractCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            print("Usage: subtract <number1> <number2>")
            return
        try:
            a = Decimal(args[0])
            b = Decimal(args[1])
            result = subtract(a, b)
            print(result)
        except Exception as e:
            print(f"Error: {e}")