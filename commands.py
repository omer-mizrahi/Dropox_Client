class CommandResponse:
    def __init__(self):
        self.valid = False
        self.messages = []
        self.position = ""


class CommandRequest:
    def __init__(self, pos, command):
        self.command = command.lower()
        self.position = pos
        self.command_type = 0
        self.entry_name = ""

    def get_type_command(self):
        # TODO : logic of get type
        if (self.command == "cd.." or self.command == "cd .."):
            self.command_type = 1

        elif (self.command.startswith("cd ")):
            self.command_type = 2
            self.entry_name = self.command.split("cd ")[1]

        elif (self.command == "dir" or self.command == "dirlist"):
            self.command_type = 3

        elif (self.command.startswith("download ")):
            self.command_type = 4
            self.entry_name = self.command.split("download ")[1]

        else:
            self.command_type = 0

        return self.command_type
