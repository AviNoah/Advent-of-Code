from typing import Literal, Union

Directions = Literal["up", "down", "right", "left"]
Spaces = Literal[".", "/", "\\", "-", "|"]

with open("input.txt", "r") as f:
    lines: list = [line.strip() for line in f.readlines()]

ROWS: int = len(lines)
COLS: int = len(lines[0])


class LightBeam:
    row: int
    col: int
    beam_dir: Directions

    def __init__(self, row: int, col: int, beam_dir: Directions):
        self.row = row
        self.col = col
        self.beam_dir = beam_dir

    def move(self) -> Union["LightBeam", None]:

        split_beam = self._direction(lines[self.row][self.col])
        self._step()

        return split_beam

    def out_of_bounds(self) -> bool:
        if self.row > ROWS or self.row < 0:
            return True
        elif self.col > COLS or self.col < 0:
            return True

        return False

    def _direction(self, next_char: Spaces) -> Union["LightBeam", None]:
        reflection: dict

        match next_char:
            case "/":
                reflection = {
                    "up": "right",
                    "right": "up",
                    "down": "left",
                    "left": "down",
                }

                self.beam_dir = reflection[self.beam_dir]
            case "\\":
                reflection = {
                    "up": "left",
                    "left": "up",
                    "down": "right",
                    "right": "down",
                }
                self.beam_dir = reflection[self.beam_dir]
            case "-":
                if self.beam_dir in ["up", "down"]:
                    self.beam_dir = "right"
                    return LightBeam(self.row, self.col, "left")
            case "|":
                if self.beam_dir in ["right", "left"]:
                    self.beam_dir = "up"
                    return LightBeam(self.row, self.col, "down")
            case ".":
                pass
            case _:
                raise Exception("Bad next char", next_char)

        return None

    def _step(self) -> None:
        match self.beam_dir:
            case "down":
                self.row += 1
            case "up":
                self.row -= 1
            case "left":
                self.col -= 1
            case "right":
                self.col += 1
            case _:
                raise Exception("bad direction")

    def __repr__(self) -> str:
        return f"({self.row}, {self.col}) {self.beam_dir}"


def part1() -> None:
    beams: list[LightBeam] = []
    beams.append(LightBeam(0, 0, "right"))

    while beams:
        for beam in beams:
            split_beam: LightBeam | None = beam.move()

            if beam.out_of_bounds():
                beams.remove(beam)

            if split_beam:
                beams.append(split_beam)


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
