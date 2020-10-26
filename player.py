class Player:
    """Base class for a player."""
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    def add_score(self, score):
        self.total_score += score

    def reset_score(self):
        self.total_score = 0

    def take_turn(self, roll_die):
        """Abstract method for taking a turn. To be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement the take_turn method.")


class HumanPlayer(Player):
    """Class for a human player."""
    def take_turn(self, roll_die):
        print(f"\n{self.name}'s turn.")
        turn_score = 0
        while True:
            print(f"Total score: {self.total_score}")
            print(f"Turn score: {turn_score}")
            choice = input("Roll or Hold? (r/h): ").lower()
            if choice == 'r':
                roll = roll_die()
                print(f"You rolled: {roll}")
                if roll == 1:
                    print("Rolled a 1! No points this turn.")
                    return 0
                turn_score += roll
            elif choice == 'h':
                print(f"{self.name} holds with {turn_score} points.")
                return turn_score
            else:
                print("Invalid choice! Please choose 'r' to roll or 'h' to hold.")


class ComputerPlayer(Player):
    """Class for a computer player."""
    def take_turn(self, roll_die):
        print(f"\n{self.name}'s turn.")
        turn_score = 0
        while turn_score < min(25, 100 - self.total_score):
            roll = roll_die()
            print(f"{self.name} rolled: {roll}")
            if roll == 1:
                print(f"{self.name} rolled a 1! No points this turn.")
                return 0
            turn_score += roll
        print(f"{self.name} holds with {turn_score} points.")
        return turn_score
