import random
from player_factory import PlayerFactory

class PigGame:
    """Core game logic."""
    def __init__(self, player1_type, player2_type):
        self.players = [
            PlayerFactory.create_player(player1_type, "Player 1"),
            PlayerFactory.create_player(player2_type, "Player 2")
        ]
        self.current_player_index = 0

    def roll_die(self):
        """Simulate rolling a 6-sided die."""
        return random.randint(1, 6)

    def switch_player(self):
        """Switch to the next player."""
        self.current_player_index = 1 - self.current_player_index

    def current_player(self):
        """Get the current player."""
        return self.players[self.current_player_index]

    def take_turn(self):
        """Handle the current player's turn."""
        player = self.current_player()
        turn_score = player.take_turn(self.roll_die)
        player.add_score(turn_score)
        if player.total_score >= 100:
            return True
        self.switch_player()
        return False
