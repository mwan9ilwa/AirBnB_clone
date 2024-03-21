import cmd
from models.base_model import BaseModel
import models.storage as storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the ID."""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = getattr(BaseModel, arg)
            instance = cls()
            instance.save()
            print(instance.id)
        except AttributeError:
            print("** class doesn't exist **")

    # Implement other methods similarly...

if __name__ == "__main__":
    HBNBCommand().cmdloop()
