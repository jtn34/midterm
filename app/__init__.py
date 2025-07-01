from app.commands import CommandHandler
from app.commands.discord.discord import DiscordCommand
from app.commands.exit.exit import ExitCommand
from app.commands.menu.menu import MenuCommand
from app.commands.greet.greet import GreetCommand
from app.commands.goodbye.goodbye import GoodbyeCommand

# Import math commands from the plugins folder
from app.plugins.add.add import AddCommand
from app.plugins.subtract.subtract import SubtractCommand
from app.plugins.multiply.multiply import MultiplyCommand
from app.plugins.divide.divide import DivideCommand

from app.commands.handler import CommandHandler

class App:
    def __init__(self):  # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        # Register built-in commands
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("discord", DiscordCommand())

        # Register plugin math commands
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

        print("Type 'exit' to exit.")

        while True:  # REPL: Read-Eval-Print Loop
            user_input = input(">>> ").strip()
            if user_input:
                self.command_handler.execute_command(user_input)