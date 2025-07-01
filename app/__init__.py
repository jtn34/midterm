from app.commands import CommandHandler
from app.commands.discord.discord import DiscordCommand
from app.commands.exit.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet.greet import GreetCommand
from app.commands.menu.menu import MenuCommand

class App:
    @staticmethod
    def start() -> None:
        print("Hello World. Type 'exit' to exit.")
        
        while True:
            user_input = input(">>> ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            else:
                # Here, you could add additional commands and their handling
                print("Unknown command. Type 'exit' to exit.")

    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        # Register commands here
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("discord", DiscordCommand())

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())