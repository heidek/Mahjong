class Tile:
    def __init__(self, value=None, suit=None):
        self.value = value
        self.suit = suit

    def __repr__(self):
        '''Tile[1, 'm'] --> "1m"'''
        return str(self.value) + str(self.suit)

    def __lt__(self, other):
        '''Enables ordering of hand, by suits and values.'''
        if self.suit != other.suit:
            suit_to_num = {
                'm': 0,
                'p': 1,
                's': 2,
                'h': 3,
            }
            return suit_to_num[self.suit] < suit_to_num[other.suit]
        else:
            return self.value < other.value

    def __eq__(self, other):
        '''Tiles are equal when suit and value are equal'''
        return self.suit == other.suit and self.value == other.value


class Hand:
    def __init__(self, tiles=[]):
        self.tiles = tiles
        self.tiles.sort()

    def __repr__(self):
        '''Enables standard readout of a hand "111m222p333sEEEWW'''
        out = ''
        man = []
        pin = []
        sou = []
        honor = []
        for tile in self.tiles:
            if tile.suit == 'm':
                man.append(tile)
            elif tile.suit == 'p':
                pin.append(tile)
            elif tile.suit == 's':
                sou.append(tile)
            elif tile.suit == 'h':
                honor.append(tile)
        for tile in man:
            out = out + str(tile.value)
        if man:
            out = out + 'm'
        for tile in pin:
            out = out + str(tile.value)
        if pin:
            out = out + 'p'
        for tile in sou:
            out = out + str(tile.value)
        if sou:
            out = out + 's'
        for tile in honor:
            out = out + str(tile.value)
        return out

    def __len__(self):
        return len(self.tiles)

    def __eq__(self, other):
        return self.tiles == other.tiles

    def remove(self, to_remove):
        if to_remove:
            for tile in to_remove.copy():
                self.tiles.remove(tile)
