'''
Class CommandHandler acts as the invoker. It stores commands and knows how to execute them 
based on user input. 
An empty dictionary commands is the constructor method. Maps command names to command objects.
register_command: registers a command with a name.
execute_command: takes a single string from user input to parse, find correct command, 
converts arguments to Decimal, and runs the command.
'''
from abc import ABC, abstractmethod
from decimal import Decimal
from app.commands import CommandHandler
from app.commands.discord import DiscordCommand
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.menu import MenuCommand

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass # pragma: no cover

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, command):
        self.commands[command_name.lower()] = command

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
    
    def execute_command(self, command_line):
        try:
            parts = command_line.strip().split()
        except AttributeError:
            print("Command must be a string.")
            return
    
        if not parts:
            print("No command was entered.")
            return
    
        command_name = parts[0].lower()
        args = parts[1:]
        
        try:
            command = self.commands[command_name]
            decimal_args = [Decimal(arg) for arg in args]
            result = command.execute(*decimal_args)
            print(f"Result: {result}")
        except KeyError:
            print(f"Unknown command: {command_name}")
        except Exception as e:
            print(f"Error in executing {command_name}: {e}")
    
    def execute_command(self, command_name: str):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")

class App:
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