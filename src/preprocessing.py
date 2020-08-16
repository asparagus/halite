import numpy as np


class Preprocessor:
    def __init__(self, padding):
        self.padding = padding

    def process(self, board):
        return np.array([
            Preprocessor.pad(f, self.padding)
            for f in (
                Preprocessor.halite_filter(board),
                Preprocessor.ship_filter(board),
                Preprocessor.shipyard_filter(board),
            )
        ])

    @classmethod
    def pad(cls, filter_, width):
        return np.pad(
            filter_, 
            [(width, width), (width, width)], 
            mode='wrap'
        )

    @classmethod
    def unpad(cls, filter_, width):
        return filter_[width:-width, width:-width]

    @classmethod
    def halite_filter(cls, board):
        size = board.configuration.size
        halite = np.zeros([size, size])
        for x in range(size):
            for y in range(size):
                halite[y][x] = board[(x, y)].halite
        return halite

    @classmethod
    def ship_filter(cls, board):
        size = board.configuration.size
        ships = np.zeros([size, size])
        for player_id, player in board.players.items():
            for ship in player.ships:
                x, y = ship.position
                ships[(y, x)] = (1 if player_id == board.current_player_id else -1)
        return ships
    
    @classmethod
        def ship_cargo(cls, board):
            size = board.configuration.size
            ships = np.zeros([size, size])
            for player_id, player in board.players.items():
                for ship in player.ships:
                    x, y = ship.position
                    ships[(y, x)] = (1 if player_id == board.current_player_id else -1)
            return ships

    @classmethod
    def shipyard_filter(cls, board):
        size = board.configuration.size
        shipyards = np.zeros([size, size])
        for player_id, player in board.players.items():
            for shipyard in player.shipyards:
                x, y = shipyard.position
                shipyards[(y, x)] = (1 if player_id == board.current_player_id else -1)
        return shipyards
