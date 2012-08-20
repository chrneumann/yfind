from datetime import date
from functools import reduce
import operator as op

from modgrammar import Grammar
from modgrammar import L
from modgrammar import WORD
from modgrammar import LIST_OF
from modgrammar import OPTIONAL
from modgrammar import ParseError


class Operator(Grammar):
    op_map = {
        '==': op.eq,
        '<': op.lt,
        '>': op.gt,
        '>=': op.ge,
        '<=': op.le,
        '!=': op.ne,
    }
    grammar = reduce(op.or_, [L(item) for item in op_map.keys()])

    def satisfied_by(self, left, right):
        op = self.op_map[self.elements[0].string]
        return op(left, right)


class Year(Grammar):
    grammar = WORD("0-9", count=4)


class Month(Grammar):
    grammar = WORD("0-9", min=1, max=2)


class Day(Grammar):
    grammar = WORD("0-9", min=1, max=2)


class Date(Grammar):
    grammar_whitespace = False
    grammar = (Year, '/', Month, '/', Day)

    def value(self, data=None):
        return date(int(self.elements[0].string),
                    int(self.elements[2].string),
                    int(self.elements[4].string))


class Scalar(Grammar):
    grammar_whitespace = False
    grammar = ('"', WORD(r'^\"'), '"')

    def value(self, data=None):
        return self.elements[1].string


class Floating(Grammar):
    grammar_whitespace = False
    grammar = WORD("0-9.")

    def value(self, data=None):
        return float(self.elements[0].string)


class Integral(Grammar):
    grammar_whitespace = False
    grammar = WORD("0-9")

    def value(self, data=None):
        return int(self.elements[0].string)


class FieldValue(Grammar):
    grammar = (Date | Floating | Integral)

    def value(self, data=None):
        return self.elements[0].value(None)


class Identifier(Grammar):
    grammar_whitespace = False
    grammar = (WORD("A-Za-z_"), OPTIONAL(L("["), WORD("0-9"), L("]")))


class Node(Grammar):
    grammar_whitespace = False
    grammar = (L('.'), LIST_OF(Identifier, sep='.', min=1))

    def _parse_value(self, exp):
        if isinstance(exp, str) or isinstance(exp, bytes):
            try:
                operand = FieldValue.parser().parse_string(exp, eof=True)
                return operand.value()
            except ParseError:
                pass
        return exp

    def value(self, data):
        pos = data
        for element in self.elements[1]:
            if element.string == '.':
                continue
            if pos.get(element[0].string, None) is None:
                return None
            pos = pos[element[0].string]
            if element[1] is not None:
                pos = pos[int(element[1][1].string)]
        return self._parse_value(pos)


class Operand(Grammar):
    grammar = (Node | Date | Scalar | Floating | Integral)

    def value(self, data):
        return self.elements[0].value(data)


class SearchGrammar(Grammar):
    """Grammar for search expressions."""
    grammar = (Operand, Operator, Operand)

    @staticmethod
    def matches(data, exp):
        tree = SearchGrammar.parser().parse_string(exp, eof=True)
        (left, op, right) = tree.elements
        if left.value(data) is None or right.value(data) is None:
            return False
        return op.satisfied_by(left.value(data), right.value(data))


def matches(data, expression):
    """Check if data satisfies the expression.
    """
    return SearchGrammar.matches(data, expression)
