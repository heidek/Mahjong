import pytest
from Mahjong.classes.classes import *
from Mahjong.win_check import triplet_search


class TestClass:
    def test_null(self):
        x = Hand()
        assert triplet_search(x) == []

    def test_triplet(self):
        x = Hand([Tile(1, 'm'), Tile(1, 'm'), Tile(1, 'm')])
        assert triplet_search(x) == [[Tile(1, 'm'), Tile(1, 'm'), Tile(1, 'm')]]

    def test_two_triplet(self):
        x = Hand([
                Tile(1, 'm'), Tile(1, 'm'), Tile(1, 'm'),
                Tile(2, 'm'), Tile(2, 'm'), Tile(2, 'm'),
            ])
        assert triplet_search(x) == [
                                    [Tile(1, 'm'), Tile(1, 'm'), Tile(1, 'm')],
                                    [Tile(2, 'm'), Tile(2, 'm'), Tile(2, 'm')]
                                ]

    def test_neg(self):
        x = Hand([Tile(1, 'm'), Tile(1, 'm'), Tile(2, 'm')])
        assert triplet_search(x) == []
