# Card X: winning set | lotted numbers
# Point calculation: 2^(n-1) where n is the amount of matching winning numbers from the lot or 0

with open("input.txt", "r") as f:
    lines: list = f.readlines()


class card:
    def __init__(self, id: int, winning_set: set, lottery_set: set):
        self.id = int(id)
        self.winning_set = winning_set
        self.lottery_set = lottery_set

    def get_winning_lots(self) -> list:
        winning_lots: list = [
            lot for lot in self.lottery_set if lot in self.winning_set
        ]
        return winning_lots

    def calculate_score(self) -> int:
        power = len(self.get_winning_lots())
        return 2 ** (power - 1)

    def __str__(self):
        lots = self.get_winning_lots()
        return f"Card {self.id} has {len(lots)} winning numbers ({', '.join(lots)}, so it is worth {self.calculate_score()} points.)"


def main():
    return


if __name__ == "__main__":
    main()
