import re

with open("input.txt", "r") as f:
    lines = f.readlines()


class race:
    def __init__(
        self,
        max_time: int,
        max_dist: int,
    ):
        self.max_time = int(max_time)  # In ms
        self.max_dist = int(max_dist)  # In mm


class race_boat:
    def __init__(self, velocity: int = 0):
        self.velocity = velocity  # in mm/ms

    def charge(self, time: int) -> int:
        # Charge boat for time ms, return velocity in mm/ms
        acc = 1  # 1mm/ms^2
        return self.velocity + time * acc

    def accelerate(self, time: int) -> int:
        # Add charge to velocity and return new velocity
        self.velocity = self.charge(time)
        return self.velocity

    def race(self, time: int, race: race) -> bool:
        # Start a race, return whether or not we won
        vel = self.charge(time)
        dt = race.max_time - time

        return vel * dt > race.max_dist


def get_races() -> list[race]:
    global lines
    time: list = re.findall("\d+", lines[0])
    dist: list = re.findall("\d+", lines[1])

    races: zip = zip(time, dist)
    races: list[race] = [race(time, dist) for time, dist in races]
    return races


def main():
    races: list[race] = get_races()
    print(races)


if __name__ == "__main__":
    main()
