import importlib
import os
import sys
import pandas as pd
from typing import Dict, Type

class Command:
    def execute(self, *args):
        raise NotImplementedError("Execute method must be implemented by subclasses.")

class CommandFactory:
    commands: Dict[str, Type[Command]] = {}

    @classmethod
    def load_plugins(cls, plugin_dir="plugins"):
        sys.path.insert(0, plugin_dir)
        for filename in os.listdir(plugin_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = filename[:-3]
                module = importlib.import_module(module_name)
                for item_name in dir(module):
                    item = getattr(module, item_name)
                    if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                        cls.commands[module_name] = item

    @classmethod
    def get_command(cls, name: str) -> Command:
        if name in cls.commands:
            return cls.commands[name]()
        raise ValueError(f"Command '{name}' not found.")

    @classmethod
    def list_commands(cls):
        return list(cls.commands.keys())

class MenuCommand(Command):
    def execute(self, *args):
        print("Available Commands:")
        for command in CommandFactory.list_commands():
            print(f"- {command}")

class HistoryManager:
    def __init__(self, filepath='history.csv'):
        self.filepath = filepath
        self.columns = ['operation', 'operands', 'result']
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.filepath):
            pd.DataFrame(columns=self.columns).to_csv(self.filepath, index=False)

    def add_record(self, operation, operands, result):
        df = pd.read_csv(self.filepath)
        new_row = pd.DataFrame([[operation, operands, result]], columns=self.columns)
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(self.filepath, index=False)

    def load_history(self):
        return pd.read_csv(self.filepath)

    def clear_history(self):
        pd.DataFrame(columns=self.columns).to_csv(self.filepath, index=False)

    def delete_history_file(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

if __name__ == "__main__":
    CommandFactory.load_plugins()
    menu = MenuCommand()
    menu.execute()

    history = HistoryManager()
    history.add_record("add", "2,3", 5)
    print("\nCurrent History:")
    print(history.load_history())
