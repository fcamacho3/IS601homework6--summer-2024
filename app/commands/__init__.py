from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class CommandHandler:
    def __init__(self):
        self.commands = {} # Stores Dictionary of commands that are registered

    def register_command(self, command_name: str, command: Command):
        ''' Any new Command_Name and Command-type command are passed in, 
        Register them into self.commands Dictonary such that key = command_name and command is the value'''
        self.commands[command_name] = command
        
    def execute_command(self, command_line):
        '''Executes command while safely handling parameters where needed'''

        # tests if entry string is splittable. Splittable = Something was entered
        try:
            parts = command_line.split()
            command_name = parts[0]
        except IndexError:
            print("No command entered.")
            return
        
        # SOMETHING was entered, might not be a command
        command = self.commands.get(command_name)
        


        if command: # if command is not null

            #get arguments if exists
            args = parts[1:]

            # Execute command with args as potential parameter
            try:
                result = command.execute(*args)
                if result is not None: 
                    print(result)
                # print(result)
            except Exception as e:
                print(f"Error executing command '{command_name}': {e}")
        else:
            print(f"Command '{command_name}' not found.")