from typing import Iterable

DIGIT_WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


class WordFSM:
    def __init__(self, word: str, return_value: int) -> None:
        self._word = word
        self._return_value = return_value
        self._position = 0
        self._end_position = len(word) - 1

    def read_char(self, char: str) -> int | None:
        if self._word[self._position] == char:
            self._position += 1
        else:
            self._position = 0
        if self._position != self._end_position:
            return None
        self._position = 0
        return self._return_value


class DigitFinder:
    def __init__(self, include_words: bool = False):
        self._words = (
            [WordFSM(word, i) for i, word in enumerate(DIGIT_WORDS, 1)]
            if include_words
            else []
        )

    def find_digits(self, line: str) -> Iterable[int]:
        for char in line:
            if (digit := self.get_digit(char)) is not None:
                yield digit
            for fsm in self._words:
                if (digit := fsm.read_char(char)) is not None:
                    yield digit

    def get_digit(self, char: str) -> int | None:
        try:
            return int(char)
        except ValueError:
            return None


def get_calibration_value(digit_finder: DigitFinder, line: str) -> int:
    digits = list(digit_finder.find_digits(line))
    return digits[0] * 10 + digits[-1]


def get_calibration_sum(lines: list[str], include_words: bool) -> int:
    digit_finder = DigitFinder(include_words)
    return sum(get_calibration_value(digit_finder, line) for line in lines)


if __name__ == "__main__":
    with open("01.txt", "r") as f:
        lines = f.readlines()
    print(get_calibration_sum(lines, False))
    print(get_calibration_sum(lines, True))
