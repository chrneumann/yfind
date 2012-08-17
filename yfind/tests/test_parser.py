class TestGrammar(object):
    def test_search(self):
        from yfind.parser import parse_search_exp
        from yfind.parser import Operator
        res = parse_search_exp(".foo.bar = .foo")
        assert len(res.elements) == 3
        assert isinstance(res[1], Operator)
