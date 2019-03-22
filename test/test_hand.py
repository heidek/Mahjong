import pytest
from Mahjong.classes.classes import Tile, Hand


class TestClass:
    def test_init(self):
        x = Hand()
        assert x.tiles == []

    def test_init_sort(self):
        x = Hand([Tile(2, 'm'), Tile(1, 'm')])
        assert x == Hand([Tile(1, 'm'), Tile(2, 'm')])

    def test_init_string(self):
        x_tiles = '123m123p123s'
        x = Hand(x_tiles)
        assert x.tiles == [
            Tile(1, 'm'), Tile(2, 'm'), Tile(3, 'm'),
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(1, 's'), Tile(2, 's'), Tile(3, 's'),
        ]

    def test_repr(self):
        x = Hand([
            Tile(1, 'm'), Tile(1, 'm'), Tile(1, 'm'), Tile(2, 'm'), Tile(3, 'm'),
            Tile(4, 'm'), Tile(5, 'm'), Tile(6, 'm'), Tile(7, 'm'), Tile(8, 'm'),
            Tile(9, 'm'), Tile(9, 'm'), Tile(9, 'm'),
        ])
        y = Hand([Tile(1, 'm'), Tile(1, 's'), Tile(1, 'p')])
        assert str(x) == '1112345678999m' and str(y) == '1m1p1s'

    def test_repr_null(self):
        x = Hand()
        assert str(x) == ''

    def test_eq(self):
        x = Hand([Tile(1, 'm'), Tile(2, 'm')])
        y = Hand([Tile(1, 'm'), Tile(2, 'm')])
        assert x == y

    def test_remove_none(self):
        x = Hand([Tile(1, 'm'), Tile(2, 'm')])
        x.remove(None)
        assert x == Hand([Tile(1, 'm'), Tile(2, 'm')])

    def test_remove_all(self):
        x = Hand([Tile(1, 'm'), Tile(2, 'm')])
        x.remove(x.tiles)
        assert not x.tiles

    def test_remove_partial(self):
        x = Hand([Tile(1, 'm'), Tile(2, 'm')])
        x.remove([Tile(1, 'm')])
        assert x == Hand([Tile(2, 'm')])
