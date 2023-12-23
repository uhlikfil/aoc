class Card:
    def __init__(self, line: str) -> None:
        _, numbers = line.split(":")
        winning, scratched = numbers.split("|")
        self._winning_numbers = {int(n) for n in winning.split()}
        self._scratched_numbers = {int(n) for n in scratched.split()}
        self.count = 1

    @property
    def value(self) -> int:
        return len(self._winning_numbers.intersection(self._scratched_numbers))

    @property
    def points(self) -> int:
        if not self.value:
            return 0
        return 2 ** (self.value - 1)


def process_card_counts(cards: list[Card]) -> int:
    for i, card in enumerate(cards):
        start = i + 1
        for j in range(start, start + card.value):
            if j < len(cards):
                cards[j].count += card.count
    return sum(c.count for c in cards)


if __name__ == "__main__":
    with open("04.txt", "r") as f:
        lines = f.readlines()

    cards = [Card(line) for line in lines]
    print(sum(c.points for c in cards))
    print(process_card_counts(cards))
