=====
yfind
=====

Search YAML files satisfying specified conditions.

Depends on Python 3.

Examples:
``yfind '.mailings[0].sent < 2012/06/12' my_files/``

``yfind '.id == 10'``

``((?.id) and (yfind '.id == 10)) or (.enabled == "False")'``

Currently supported search expressions:

<Operand> <Operator> <Operand>

where Operator is one of ==, !=, <, >, <= or >=.

Operands may be numbers (1, 3.0), scalars ("foo", "bar"), dates
(2007/12/30) or YAML fields (.foo.bar, .foo[4].bar, .bar).

To check for existance of a field, use '?' before the field name:
``?.foo.bar``.

Search expression can be combined with the logical operators "and, or,
not":

- not (<SearchExpression>)
- (<SearchExpression>) and (<SearchExpression>)
- (<SearchExpression>) or (<SearchExpression>)

