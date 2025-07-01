from app.commands import Command
from decimal import Decimal
from calculator.operations import add

class AddCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            print("Usage: add <number1> <number2>")
            return
        try:
            a = Decimal(args[0])
            b = Decimal(args[1])
            result = add(a, b)
            print(result)
        except Exception as e:
            print(f"Error: {e}")