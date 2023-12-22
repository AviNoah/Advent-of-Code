card_types: list = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_dict: list = [(type, i) for i, type in enumerate(card_types)]
card_dict: dict = dict(card_dict)

wild_cards: bool = False

import re

with open("input.txt", "r") as f:
    lines: list = f.readlines()


class hand:
    def __init__(self, cards: list[str], bid: int):
        self.cards = cards
        self.bid = int(bid)

    def count_uniques(self) -> dict:
        # A hand is a list of 5 cards
        # Return a dictionary that shows how many times each card appears
        uniques: dict = dict()
        for card in self.cards:
            if not card in uniques.keys():
                uniques[card] = 0  # Initialize

            uniques[card] += 1

        return uniques

    @staticmethod
    def evaluate_type(d: dict, key: str) -> int:
        # Return type of hand using d and key, return value of type,
        # doesn't alter dict at the end besides setting J's to used wild card 1's

        # Return the amount of pairs found
        # High-0; two-1; three-2; full-house-3; four-4; five-5
        # The amount of pairs is always count of unique - 1

        val_max: int = d.pop(key, 1)
        return_val: int = val_max - 1  # Subtract one from amount of pairs
        sub_max_key: str = max(d, key=d.get)

        # If J is the key or sub-key, one is added to the pairs, that's it

        if key == "J" or sub_max_key == "J":
            # Wild card rules
            tmp = d.pop(sub_max_key)  # Find new sub_max_key
            
            new_sub_max_key: str = max(d, key=d.get)
            return_val += hand.evaluate_type(d, new_sub_max_key)
            
            d[sub_max_key] = tmp
            return_val += 1
        else:
            ...
        d[key] = val_max  # Return dict's state to normal
        return return_val

    def compare_uniques(self, other) -> bool | None:
        # Compare uniques with another, return True if self's type is better, false if it is lesser,
        # or None if it is equal
        global wild_cards
        s_uniq: dict = self.count_uniques()
        o_uniq: dict = other.count_uniques()

        while len(s_uniq) != 0 and len(o_uniq) != 0:
            # Keys
            key_s_uniq: str = max(s_uniq, key=s_uniq.get)
            key_o_uniq: str = max(o_uniq, key=o_uniq.get)

            s_val: int = s_uniq[key_s_uniq]
            o_val: int = o_uniq[key_o_uniq]

            if wild_cards:
                # Turn J's into USED wild cards once they are used
                s_val = self.evaluate_type(s_uniq, key_s_uniq)
                o_val = self.evaluate_type(o_uniq, key_o_uniq)

            # Check if it has a higher rank by having more uniques
            if s_val > o_val:
                return True
            elif o_val > s_val:
                return False

            # Same count of uniques, check for sub uniques
            s_uniq.pop(key_s_uniq)
            o_uniq.pop(key_o_uniq)

        return None

    def __eq__(self, other):
        # Both have same unique card counts, and have the same cards
        return self.cards == other.cards

    def __gt__(self, other):
        global card_dict

        result = self.compare_uniques(other)
        if result is not None:
            return result

        for c1, c2 in zip(self.cards, other.cards):
            if card_dict[c1] > card_dict[c2]:
                return True
            elif card_dict[c1] < card_dict[c2]:
                return False
        return False  # They are equal

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return other > self

    def __le__(self, other):
        return other > self or self == other


def get_hands() -> list[hand]:
    global lines
    hand_pattern = r"([\d\S]+) (\d+)"
    hands: list[re.Match] = [re.match(hand_pattern, line) for line in lines]
    hands: list[hand] = [hand(match.group(1), match.group(2)) for match in hands]

    return hands


def part1():
    hands: list[hand] = get_hands()
    hands: list[hand] = sorted(hands)

    payout: list[int] = [hand.bid * (i + 1) for i, hand in enumerate(hands)]
    print(sum(payout))


def part2():
    global card_dict, wild_cards
    card_types: list = [
        "1",
        "J",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "T",
        "Q",
        "K",
        "A",
    ]
    # J cards are now wild cards who can INCREASE RANK by changing the hand's type
    # "1" cards don't really exist, they are meant to represent USED wild cards

    wild_cards = True
    card_dict = [(type, i) for i, type in enumerate(card_types)]
    card_dict = dict(card_dict)

    # Give them both the same value
    card_dict["1"] = card_dict["J"]

    part1()  # Same logic


def main():
    part1()  # Solution was 249638405
    part2()  # Prev solution was 249437567


if __name__ == "__main__":
    main()
