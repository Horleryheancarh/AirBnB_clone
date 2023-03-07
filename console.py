#!/usr/bin/python3
"""
Entry to command line
"""
import cmd
import json
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.city import City


class HBNBCommand(cmd.Cmd):
    """
    Command Handler
    """

    prompt = '(hbnb) '
    l_class = []
    l_c = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """
        Parse command input
        """

        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cmnd = cls[1].split('(')
            args = cmnd[1].split('(')

            if cls[0] in HBNBCommnd.l_class and cmnd[0] in HBNBCommand.l_c:
                arg = cmnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """
        Prints help message
        """
        print('Provides Description of a given command')

    def emptyline(self):
        """
        Do Nothing
        """
        pass

    def do_count(self, cls_name):
        """
        COunt number of instances of a class
        """
        count = 0
        all_objs = storage_all()
        for key, value in all_objs.items():
            clss = key.split('.')
            if clss[0] == cls_name:
                count += 1

        print(count)

    def do_create(self, cls_name):
        """
        creates an instance of a class
        """

        if not type_model:
            print('** class name missing **')
        elif type_model not in HBNBCommand.l_classes:
            print('** class doesn\'t exist **')
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            my_model = dct[type_model]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """
        Show atring rep of instance passed
        """

        if not arg:
            print('** class name missing **')
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    print(value)
                    return
            print('** no instance found **')

    def do_update(self, arg):
        """
        Update an instance
        """

        if not arg:
            print('** class name missing **')
            return

        a = ''
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.l_classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    if len(args) == 2:
                        print('** attribute name missing **')
                    elif len(args) == 3:
                        print('** value missing **')
                    else:
                        setattr(value, args[2], args[3])
                        storage.save()
                    return
            print('** no instance found **')

    def do_destroy(self, arg):
        """
        Deletes an instance
        """

        if not arg:
            print('** class name missing **')
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    del value
                    del storage.__FileStorage__objects[key]
                    storage.save()
                    return

            print('** no instance found **')

    def do_all(self, arg):
        """
        Prints string rep of all instances
        """

        if not arg:
            print('** class name missing **')
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                if obj_name == args[0]:
                    list_instances += [value.__str__()]
                    return
            print(list_instances)

    def do_quit(self, line):
        """
        Exit command line
        """
        return True

    def do_EOF(self, line):
        """
        EOF to command line
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
