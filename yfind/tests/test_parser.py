class TestGrammar(object):
    def test_search(self):
        from yfind.parser import SearchGrammar
        from yfind.parser import Operator
        res = SearchGrammar.parser().parse_string(".foo.bar == .foo", eof=True)
        assert len(res.elements) == 3
        assert isinstance(res[1], Operator)

    def test_ops(self):
        from yfind.parser import matches
        data = {
            'foo': {'bar': 5},
            'bar': [1, 2, 3],
        }
        assert matches(data, ".foo.bar > .bar[2]")
        assert matches(data, "4 < .foo.bar")
        assert matches(data, ".bar[1] == 2")
        assert not matches(data, ".bar[1] != 2")
        assert matches(data, ".bar[0] <= 1")
        assert matches(data, ".foo.bar >= 5")

    def test_date(self):
        from yfind.parser import matches
        data = {
            'foo': "2008/11/5",
        }
        assert matches(data, ".foo == 2008/11/05")
        assert matches(data, ".foo > 2007/10/15")
        assert matches(data, ".foo < 2008/12/04")
