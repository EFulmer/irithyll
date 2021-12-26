from irithyll import irithyll


class TestAnd:
    def test_commutativity(self):
        # TODO: good place to use parametrize
        a, b = irithyll.F(), irithyll.F()
        assert irithyll.And(a, b).evaluate() == irithyll.And(b, a).evaluate()

        c, d = irithyll.T(), irithyll.F()
        assert irithyll.And(c, d).evaluate() == irithyll.And(d, c).evaluate()

        e, f = irithyll.F(), irithyll.T()
        assert irithyll.And(e, f).evaluate() == irithyll.And(f, e).evaluate()

        g, h = irithyll.T(), irithyll.T()
        assert irithyll.And(g, h).evaluate() == irithyll.And(h, g).evaluate()


class TestNot:
    pass
