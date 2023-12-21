class race:
    def __init__(
        self,
        max_time: int,
        max_dist: int,
    ):
        self.max_time = max_time  # In ms
        self.max_dist = max_dist  # In mm


class race_boat:
    def __init__(self, races: list[race], velocity: int = 0):
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


def main():
    return


if __name__ == "__main__":
    main()
