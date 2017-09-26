"""Single Responsibility Principle
Testing and checking SRP of SOLID
"""

from abc import ABCMeta, abstractmethod


class Book(object):
    """
    Class for printing, changing page and storing books.
    """

    def get_title(self):
        """
        print books name
        :return:
        """
        return "The Alchemist"

    def get_author(self):
        """
        return author name of the book
        :return:
        """
        return "Paulo Coelho"

    def turn_page(self):
        """
        pointer to the next page
        :return:
        """
        pass

    def print_current_page(self):
        """
        print current page content
        :return:
        """
        # Here, this violates SRP. What if we want to print it in on-screen, text-only, graphical-ui. we need to change
        # code which violates SRP. Each class should have only one reason to change.
        print "And, when you want something, all the universe conspires in helping you to achieve it."


def main():
    book = Book()
    book.print_current_page()


if __name__ == '__main__':
    main()