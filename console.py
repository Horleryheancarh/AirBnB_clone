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

    prompt = ''
