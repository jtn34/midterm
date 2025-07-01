class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, input_line):
        parts = input_line.strip().split()
        if not parts:
            return
        name = parts[0]
        args = parts[1:]

        command = self.commands.get(name)
        if command:
            command.execute(*args)
        else:
            print(f"No such command: {input_line}")