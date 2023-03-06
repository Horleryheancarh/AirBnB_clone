#!/usr/bin/python3
"""
Entry to command line
"""
import cmd
from models import storage
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Command Handler
    """

    prompt = '(hbnb) '
    l_class = []
    l_c = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """Parse command input"""
        if '.' in arg and  '(' in arg and ')' in arg:
            cls = arg.split('.')
            cmnd = cls[1].split('(')
            args = cmnd[1].split('(')

            if cls[0] in HBNBCommnd.l_class and cmnd[0] in HBNBCommand.l_c:
                arg = cmnd[0] + ' ' +  cls[0] + ' ' + args[0]
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
