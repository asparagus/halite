from kaggle_environments.envs.halite.helpers import Board


class Model:
    def __init__(self, board_size):
        self.board_size = board_size

    def act(self, board):
        raise NotImplementedError()


class ConstantModel(Model):
    def __init__(self, board_size, action):
        self.board_size = board_size
        self.action = action

    def act(self, board):
        current_player = board.current_player
        for ship in current_player.ships:
            ship.next_action = self.action
        return current_player.next_actions


def model_agent(model):
    def act(observation, configuration):
        board = Board(observation, configuration)
        return model.act(board)
    return act
