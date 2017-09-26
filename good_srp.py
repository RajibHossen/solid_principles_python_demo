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
        # This is expected and obey SRP
        return "And, when you want something, all the universe conspires in helping you to achieve it."


class Printer(object):
    """
    Interface for implementing printing functionality for different types
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def print_page(self, page):
        pass


class PlainTextPrinter(Printer):

    def print_page(self, page):
        print page


class HTMLPrinter(Printer):

    def print_page(self, page):
        print "<div style='single-page'> %s </div>" % page


def main():
    book = Book()
    texts = book.print_current_page()
    plain_text_printer = PlainTextPrinter()
    plain_text_printer.print_page(texts)

    html_printer = HTMLPrinter()
    html_printer.print_page(texts)


if __name__ == '__main__':
    main()