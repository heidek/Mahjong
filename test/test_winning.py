import pytest
from Mahjong.classes.classes import *
from Mahjong.win_check import is_winning_hand


class TestClass:
    def test_null(self):
        x = None
        assert not is_winning_hand(x)

    def test_empty(self):
        x = Hand()
        assert not is_winning_hand(x)

    def test_not_winning(self):
        x = Hand([Tile(1, 'm')])
        assert not is_winning_hand(x)

    def test_pair(self):
        x = Hand([Tile(1, 'm'), Tile(1, 'm')])
        assert is_winning_hand(x)

    def test_pair_and_sequence(self):
        x = Hand([Tile(1, 'm'), Tile(1, 'm'), Tile(1, 'm'), Tile(2, 'm'), Tile(3, 'm')])
        assert is_winning_hand(x)

    def test_pair_and_triplet(self):
        x = Hand([Tile(1, 'm'), Tile(1, 'm'), Tile(1, 'm'), Tile(2, 'm'), Tile(2, 'm')])
        assert is_winning_hand(x)

    def test_pair_and_two_sequence(self):
        x = Hand([
                Tile(1, 'm'), Tile(1, 'm'), Tile(1, 'm'), Tile(2, 'm'),
                Tile(3, 'm'), Tile(1, 'm'), Tile(2, 'm'), Tile(3, 'm')
            ])
        assert is_winning_hand(x)

    def test_pair_sequence_triplet(self):
        x = Hand([
            Tile(1, 'm'), Tile(1, 'm'), Tile(1, 'm'), Tile(2, 'm'),
            Tile(3, 'm'), Tile(2, 'm'), Tile(2, 'm'), Tile(2, 'm')
        ])
        assert is_winning_hand(x)

    def test_pair_and_two_triplet(self):
        x = Hand([
            Tile(1, 'm'), Tile(1, 'm'), Tile(1, 'm'), Tile(2, 'm'),
            Tile(2, 'm'), Tile(2, 'm'), Tile(3, 'm'), Tile(3, 'm')
        ])
        assert is_winning_hand(x)

    def test_pair_and_three_sequence(self):
        x = Hand([
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(1, 's'), Tile(2, 's'), Tile(3, 's'),
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(4, 'p'), Tile(4, 'p')
        ])
        assert is_winning_hand(x)

    def test_pair_and_two_sequence_and_triplet(self):
        x = Hand([
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(1, 's'), Tile(2, 's'), Tile(3, 's'),
            Tile(5, 'p'), Tile(5, 'p'), Tile(5, 'p'),
            Tile(4, 'p'), Tile(4, 'p')
        ])
        assert is_winning_hand(x)

    def test_pair_and_sequence_and_two_triplet(self):
        x = Hand([
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(6, 's'), Tile(6, 's'), Tile(6, 's'),
            Tile(5, 'p'), Tile(5, 'p'), Tile(5, 'p'),
            Tile(4, 'p'), Tile(4, 'p')
        ])
        assert is_winning_hand(x)

    def test_pair_and_three_triplet(self):
        x = Hand([
            Tile(7, 'p'), Tile(7, 'p'), Tile(7, 'p'),
            Tile(6, 's'), Tile(6, 's'), Tile(6, 's'),
            Tile(5, 'p'), Tile(5, 'p'), Tile(5, 'p'),
            Tile(4, 'p'), Tile(4, 'p')
        ])
        assert is_winning_hand(x)

    def test_pair_and_four_sequence(self):
        x = Hand([
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(1, 'm'), Tile(2, 'm'), Tile(3, 'm'),
            Tile(4, 'p'), Tile(4, 'p')
        ])
        assert is_winning_hand(x)

    def test_pair_and_three_sequence_and_triplet(self):
        x = Hand([
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(5, 'm'), Tile(5, 'm'), Tile(5, 'm'),
            Tile(4, 'p'), Tile(4, 'p')
        ])
        assert is_winning_hand(x)

    def test_pair_and_two_sequence_and_two_triplet(self):
        x = Hand([
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(5, 'p'), Tile(5, 'p'), Tile(5, 'p'),
            Tile(5, 'm'), Tile(5, 'm'), Tile(5, 'm'),
            Tile(4, 's'), Tile(4, 's')
        ])
        assert is_winning_hand(x)

    def test_pair_and_sequence_and_three_triplet(self):
        x = Hand([
            Tile(1, 'p'), Tile(2, 'p'), Tile(3, 'p'),
            Tile(6, 'p'), Tile(6, 'p'), Tile(6, 'p'),
            Tile(5, 'p'), Tile(5, 'p'), Tile(5, 'p'),
            Tile(5, 'm'), Tile(5, 'm'), Tile(5, 'm'),
            Tile(4, 's'), Tile(4, 's')
        ])
        assert is_winning_hand(x)

    def test_pair_and_four_triplet(self):
        x = Hand([
            Tile(3, 's'), Tile(3, 's'), Tile(3, 's'),
            Tile(6, 'p'), Tile(6, 'p'), Tile(6, 'p'),
            Tile(5, 'p'), Tile(5, 'p'), Tile(5, 'p'),
            Tile(5, 'm'), Tile(5, 'm'), Tile(5, 'm'),
            Tile(4, 'p'), Tile(4, 'p')
        ])
        assert is_winning_hand(x)
