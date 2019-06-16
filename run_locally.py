import json

from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer, Human

from bot import TossBot

def main():
    with open("botinfo.json") as f:
        info = json.load(f)

    race = Race[info["race"]]

    run_game(maps.get("Automaton LE"), [
        Bot(race, TossBot()),
        Computer(Race.Random, Difficulty.Medium)
    ], realtime=True)

if __name__ == '__main__':
    main()
