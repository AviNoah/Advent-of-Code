import re
from math import sqrt, ceil, floor
from functools import reduce

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

    def count_possible_wins(self, initial_vel: int, acc: int) -> int:
        # Count possible ways to win a race with given initial conditions (in mm/ms and mm/ms**2 respectively)
        # The function describing this movement is:
        # dist = (t*acc + initial_vel) * (max_time-t)  # this is a parabola

        # to find when it is equal to max_dist, we will simplify and get:
        # dist = -acc*t**2 + t(a*max_time - initial_vel) + initial_vel * max_time

        # Lets find t when dist = max_dist
        # [-acc]*t**2 + t[(a*max_time - initial_vel)] + [initial_vel * max_time - max_dist] = 0

        A = -acc
        B = acc * self.max_time - initial_vel
        C = initial_vel * self.max_time - self.max_dist

        s_root = B**2 - 4 * A * C
        s_root = sqrt(s_root)

        # Range of answers lays between t1 and t2 -> (t2 <= t <= t1)
        t_min = -B - s_root
        t_min /= 2 * A
        t_max = -B + s_root
        t_max /= 2 * A

        if t_min > t_max:
            t_min, t_max = t_max, t_min  # Make sure max is bigger

        return floor(t_max) - ceil(t_min)  # Return range in whole integers


class race_boat:
    def __init__(self, velocity: int = 0):
        self.velocity = velocity  # in mm/ms

    def charge(self, time: int) -> int:
        # Charge boat for time ms, return velocity in mm/ms
        acc = 1  # 1mm/ms**2
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


def part1(boat: race_boat, races: list[race]) -> list[int]:
    # Count all ways to beat the record of every race
    return [race.count_possible_wins(initial_vel=0, acc=1) for race in races]


def main():
    boat: race_boat = race_boat()
    races: list[race] = get_races()
    part1_ans = part1(boat, races)
    print(reduce(lambda a, b: a * b, part1_ans))


if __name__ == "__main__":
    main()
