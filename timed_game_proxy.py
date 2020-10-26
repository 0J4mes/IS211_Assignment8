import time
from pig import PigGame

class TimedGameProxy:
    """Proxy class to add a timed aspect to the Pig game."""
    def __init__(self, game):
        self.game = game
        self.start_time = time.time()

    def play(self):
        """Play the game with a one-minute timer."""
        print("Timed version of Pig: You have one minute to play.")
        while True:
            if time.time() - self.start_time > 60:
                print("Time's up!")
                self.declare_winner()
                return
            if self.game.take_turn():
                print(f"\n{self.game.current_player().name} wins with {self.game.current_player().total_score} points!")
                return

    def declare_winner(self):
        """Declare the winner based on the highest score."""
        player1, player2 = self.game.players
        if player1.total_score > player2.total_score:
            print(f"{player1.name} wins with {player1.total_score} points!")
        elif player2.total_score > player1.total_score:
            print(f"{player2.name} wins with {player2.total_score} points!")
        else:
            print("It's a tie!")
