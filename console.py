#!/usr/bin/python3
"""This is the console for AirBnB"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models import storage

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,
    "Place": Place
}


class HBNBCommand(cmd.Cmd):
    """console class for AirBnB"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def help_quit(self):
        """Help command for quit"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help command for EOF"""
        print("EOF command to exit the program")

    def do_help(self, arg):
        """Help command for help"""
        super().do_help(arg)

    def help_help(self):
        """Help command for help"""
        print("Help command for help")

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, arg):
        """Create command to create a new instance"""
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            model = classes[arg]()
            storage.save()
            print(model.id)

    def help_create(self):
        """Help command for create"""
        print("Create command to create a new instance")

    def do_show(self, arg):
        """Show command to show an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def help_show(self):
        """Help command for show"""
        print("Show command to show an instance")

    def do_destroy(self, arg):
        """Destroy command to destroy an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def help_destroy(self):
        """Help command for destroy"""
        print("Destroy command to destroy an instance")

    def do_all(self, arg):
        """All command to show all instances"""
        args = arg.split()
        if not arg:
            for key in storage.all():
                print(storage.all()[key])
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for key in storage.all():
                if args[0] in key:
                    print(storage.all()[key])

    def help_all(self):
        """Help command for all"""
        print("All command to show all instances")

    def do_update(self, arg):
        """Update command to update an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                setattr(storage.all()[key], args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")

    def help_update(self):
        """Help command for update"""
        print("Update command to update an instance")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
