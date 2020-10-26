import argparse
from pig import PigGame
from timed_game_proxy import TimedGameProxy

def main():
    parser = argparse.ArgumentParser(description="Play the Pig game.")
    parser.add_argument("--player1", choices=["human", "computer"], required=True, help="Type of Player 1")
    parser.add_argument("--player2", choices=["human", "computer"], required=True, help="Type of Player 2")
    parser.add_argument("--timed", action="store_true", help="Enable timed mode")
    args = parser.parse_args()

    game = PigGame(args.player1, args.player2)
    if args.timed:
        proxy = TimedGameProxy(game)
        proxy.play()
    else:
        game.play()

if __name__ == "__main__":
    main()
