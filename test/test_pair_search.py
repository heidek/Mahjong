import pytest
from Mahjong.classes.classes import *
from Mahjong.win_check import pair_search


class TestClass:
    def test_null(self):
        x = Hand()
        assert pair_search(x) == []

    def test_pair(self):
        x = Hand([Tile(1, 'm'), Tile(1, 'm')])
        assert pair_search(x) == [[Tile(1, 'm'), Tile(1, 'm')]]

    def test_two_pair(self):
        x = Hand([Tile(1, 'm'), Tile(1, 'm'), Tile(2, 'm'), Tile(2, 'm')])
        assert pair_search(x) == [[Tile(1, 'm'), Tile(1, 'm')], [Tile(2, 'm'), Tile(2, 'm')]]

    def test_pair_neg(self):
        x = Hand([Tile(1, 'm'), Tile(2, 'm')])
        assert pair_search(x) == []
