#!/usr/bin/python3
"""Air bnb project console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class for console commands"""
    prompt = '(hbnb) '

    def do_quite(self, arg):
        """quit command to exit the programe"""
        return True

    def do_EOF(self, arg):
        """exits the command line at the end of file"""
        return True

    def emptyline(self):
        """does nothing when empty line is enter into input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
