from modgrammar import Grammar
from modgrammar import L
from modgrammar import WORD


class Operator(Grammar):
    grammar = (L("=") | L("<") | L(">"))


class Node(Grammar):
    grammar_whitespace = False
    grammar = (".", WORD("A-Za-z._"))


class Year(Grammar):
    grammar = WORD("0-9", count=4)


class Month(Grammar):
    grammar = WORD("0-9", min=1, max=2)


class Day(Grammar):
    grammar = WORD("0-9", min=1, max=2)


class Date(Grammar):
    grammar = (Year, '/', Month, '/', Day)


class Scalar(Grammar):
    grammar_whitespace = False
    grammar = ('"', WORD(r'^\"'), '"')


class Operand(Grammar):
    grammar = (Node | Date | Scalar)


class SearchGrammar(Grammar):
    """Grammar for search expressions."""
    grammar = (Operand, Operator, Operand)


def parse_search_exp(exp):
    """Parse string and return resulting SearchGrammer instance."""
    res = SearchGrammar.parser().parse_string(exp, eof=True)
    return res
