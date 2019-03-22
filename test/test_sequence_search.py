import pytest
from Mahjong.classes.classes import *
from Mahjong.win_check import sequence_search


class TestClass:
    def test_null(self):
        x = Hand()
        assert sequence_search(x) == []

    def test_sequence(self):
        x = Hand([Tile(1, 'm'), Tile(2, 'm'), Tile(3, 'm')])
        assert sequence_search(x) == [[Tile(1, 'm'), Tile(2, 'm'), Tile(3, 'm')]]

    def test_two_sequence(self):
        x = Hand([Tile(1, 'm'), Tile(2, 'm'), Tile(3, 'm'), Tile(2, 'm'), Tile(3, 'm'), Tile(4, 'm')])
        assert sequence_search(x) == [
                                        [Tile(1, 'm'), Tile(2, 'm'), Tile(3, 'm')],
                                        [Tile(2, 'm'), Tile(3, 'm'), Tile(4, 'm')]
                                    ]

    def test_sequence_neg(self):
        x = Hand([Tile(1, 'm'), Tile(1, 'm')])
        assert sequence_search(x) == []
