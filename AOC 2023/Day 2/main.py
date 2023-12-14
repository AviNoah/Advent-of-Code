def main(bag: dict):
    with open("input.txt", "r") as f:
        lines: list = f.readlines()
    
    def collect_max_tuple(line: str)-> tuple:
        # Given sets of subsets of picked dice, pick maximum amount of dice.
                 



if __name__ == "__main__":
    goal_bag: dict = {'red':12, 'green':13, 'blue':14}  # RGB
    main(goal_bag)
