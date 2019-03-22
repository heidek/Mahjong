from classes.classes import *


def is_winning_hand(hand):
    '''
    Returns True is hand has four sets of three and a pair.
    Process:
    - Removes a pair
    - Removes a sequence
        - Checks if removing all triplets leaves no tiles in the and
        - If so, must have removed four sets and a pair
        - If not, removes another sequence and repeats
    - Removes all triplets from original hand as a fencepost
    '''
    if hand:
        pairs = pair_search(hand)

        if pairs:
            test_hand = Hand(hand.tiles.copy())

            for pair in pairs:
                '''Tests sequence/triplet removal for each pair'''
                test_hand.remove(pair)
                if len(test_hand) == 0:  # If just one pair
                    return True
                sequences = sequence_search(test_hand)
                sequence_check_hand = Hand(test_hand.tiles.copy())  # Copy to remove sequences from
                for sequence in sequences:
                    '''Remove all triplets, if no win remove another sequence'''
                    test_hand = Hand(sequence_check_hand.tiles.copy())
                    test_hand.remove(sequence)
                    sequence_check_hand = Hand(test_hand.tiles.copy())  # Copy to put triplets back in on next loop

                    triplets = triplet_search(test_hand)
                    for triplet in triplets:
                        test_hand.remove(triplet)

                    if len(test_hand) == 0:
                        return True

                triplets = triplet_search(test_hand)  # Catches case where no sequences
                for triplet in triplets:
                    test_hand.remove(triplet)

                if len(test_hand) == 0:
                    return True
                else:
                    test_hand = Hand(hand.tiles.copy())

            return False


def pair_search(hand):
    '''
    Finds all pairs in hand without replacement
    222m -> (2m, 2m), 2222m -> (2m, 2m), (2m, 2m)
    '''
    pairs = []
    hand_copy = Hand(hand.tiles.copy())
    for tile in hand.tiles:
        pair = [tile] * 2
        if hand_copy.tiles.count(tile) >= 2:
            try:
                hand_copy.remove(pair)
                pairs.append(pair)
            except Exception as e:
                pass
    return pairs


def sequence_search(hand):
    '''Finds all sequences in hand without replacement'''
    sequences = []
    hand_copy = Hand(hand.tiles.copy())
    for tile in hand.tiles:
        if Tile(tile.value + 1, tile.suit) in hand.tiles and Tile(tile.value + 2, tile.suit) in hand.tiles:
            sequence = [tile, Tile(tile.value + 1, tile.suit), Tile(tile.value + 2, tile.suit)]
            try:
                hand_copy.remove(sequence)
                sequences.append(sequence)
            except Exception as e:
                pass
    return sequences


def triplet_search(hand):
    '''Finds all triplets in hand without replacement'''
    triplets = []
    hand_copy = Hand(hand.tiles.copy())
    for tile in hand.tiles:
        triplet = [tile] * 3
        if hand.tiles.count(tile) >= 3:
            try:
                hand_copy.remove(triplet)
                triplets.append(triplet)
            except Exception as e:
                pass
    return triplets
