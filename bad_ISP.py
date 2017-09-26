"""
Interface Segregation Principle bad example
"""

from abc import ABCMeta, abstractmethod


class IMachine(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def print_items(self):
        pass

    @abstractmethod
    def staple(self):
        pass

    @abstractmethod
    def fax(self):
        pass

    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def photocopy(self):
        pass


class Machine(IMachine):
    def scan(self):
        print "Scanning documents"

    def fax(self):
        print "Sending Fax"

    def photocopy(self):
        print "Photocopying documents"

    def print_items(self):
        print "Printing Items"

    def staple(self):
        print "Stapling items"


class Staple(IMachine):
    def scan(self):
        pass

    def fax(self):
        pass

    def print_items(self):
        pass

    def staple(self):
        print "Stapling items"

    def photocopy(self):
        pass