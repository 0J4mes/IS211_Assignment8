from player import HumanPlayer, ComputerPlayer

class PlayerFactory:
    """Factory class to create players."""
    @staticmethod
    def create_player(player_type, name):
        if player_type == "human":
            return HumanPlayer(name)
        elif player_type == "computer":
            return ComputerPlayer(name)
        else:
            raise ValueError("Invalid player type. Choose 'human' or 'computer'.")
