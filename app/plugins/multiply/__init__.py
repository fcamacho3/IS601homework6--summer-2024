from decimal import Decimal, InvalidOperation
from app.commands import Command
from app.plugins.calc.calculator import multiply

class MultiplyCommand(Command):

    def execute(self, *args):
        # Check if the correct number of arguments is provided
        if len(args) != 2:
            return "Please use 'multiply' command with two Decimal numbers as parameters."
        
        # # Attempt to convert arguments to Decimal and multiply them
        try:
            return multiply(Decimal(args[0]), Decimal(args[1]))
        except InvalidOperation:
            return "Invalid input. Please enter two Decimal numbers."
