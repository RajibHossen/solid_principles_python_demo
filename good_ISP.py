"""
Interface Segregation Principle GOOD example
"""

from abc import ABCMeta, abstractmethod


class IPrinter(object):
    """
    Interface for printing items
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def print_items(self):
        """
        items printing abstract method
        :return:
        """
        pass


class Printer(IPrinter):
    """
    Printer class for printing items and implementing printer interface
    """
    def print_items(self):
        """
        printing items here
        :return:
        """
        print "Printing items"


class IStaple(object):
    """
    Interface for stapler
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def staple(self):
        """
        abstract method for stapler class
        :return:
        """
        pass


class Staple(IStaple):
    """
    Stapler class that is responsible for stapling items
    """
    def staple(self):
        """
        stapler method
        :return:
        """
        print "Stapling items"


class IFax(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def fax(self):
        pass


class IScan(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def scan(self):
        pass


class IPhotoCopy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def photocopy(self):
        pass


class Machine(IFax, IStaple, IPhotoCopy, IPrinter, IScan):
    def print_items(self):
        print "Printing Items"

    def staple(self):
        print "Stapling items"

    def fax(self):
        print "Faxing items"

    def scan(self):
        print "Scanning items"

    def photocopy(self):
        print "Photocopying items"


def main():

    machine = Machine()
    machine.print_items()
    machine.fax()

    staplar = Staple()
    staplar.staple()

    printer = Printer()
    printer.print_items()


if __name__ == '__main__':
    main()