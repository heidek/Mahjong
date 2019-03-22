import pytest
from Mahjong.classes.classes import Tile


class TestClass:
    def test_init(self):
        x = Tile()
        assert x.value is None, x.suit is None

    def test_repr(self):
        x = Tile(1, 'm')
        print(x)
        assert str(x) == "1m"

    def test_lt(self):
        x = Tile(1, 'm')
        y = Tile(2, 'm')
        assert (x < y)

    def test_lt_neg(self):
        x = Tile(1, 'z')
        y = Tile(2, 'm')
        assert not (x < y)

    def test_eq(self):
        x = Tile(1, 'm')
        assert x == x

    def test_eq_2(self):
        x = Tile(1, 'm')
        y = Tile(1, 'm')
        assert x == y

    def test_eq_neg(self):
        x = Tile(1, 'm')
        y = Tile(1, 'p')
        assert x != y
