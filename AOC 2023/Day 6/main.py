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

        t_max_f = floor(t_max)
        t_min_c = ceil(t_min)

        possible_wins = t_max_f - t_min_c
        if t_max_f < t_max:
            possible_wins += 1

        elif t_max_f == t_max:
            possible_wins -= (
                1  # Cannot be counted as a way to win since its on the very max
            )

        if t_min_c < t_min:
            possible_wins += 1

        return possible_wins  # Return range in whole integers


def get_races(ignore_kerning: bool = False) -> list[race] | race:
    global lines
    time: list = re.findall("\d+", lines[0])
    dist: list = re.findall("\d+", lines[1])

    if ignore_kerning:
        time = "".join(time)
        dist = "".join(dist)
        return race(time, dist)

    races: zip = zip(time, dist)
    races: list[race] = [race(time, dist) for time, dist in races]
    return races


def part1():
    # Count all ways to beat the record of every race
    races: list[race] = get_races()
    part1_ans = [race.count_possible_wins(initial_vel=0, acc=1) for race in races]
    print(reduce(lambda a, b: a * b, part1_ans))


def part2():
    # Count all ways to beat the record of every race
    races: race = get_races(ignore_kerning=True)
    print(races.count_possible_wins(initial_vel=0, acc=1))


def main():
    part1()  # Solution was 160816
    part2()  # Solution was 46561107


if __name__ == "__main__":
    main()
