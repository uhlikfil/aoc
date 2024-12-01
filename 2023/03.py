import re
from typing import Iterable


class PartsInfo:
    NUM_PATTERN = re.compile(r"(\d+)")

    def __init__(self, info: str) -> None:
        self._info = info
        self._active_positions: set[int] = set()
        for i, char in enumerate(info):
            if self._is_symbol(char):
                self._active_positions.add(i)

    def activates(self, start_pos: int, end_pos: int) -> bool:
        return bool(self._active_positions.intersection(range(start_pos, end_pos + 1)))

    def get_active_numbers(
        self,
        top: "PartsInfo | None",
        bot: "PartsInfo | None",
    ) -> Iterable[int]:
        for m in self.NUM_PATTERN.finditer(self._info):
            number = int(m.group(1))
            start_pos = max(0, m.start() - 1)
            end_pos = m.end()
            print(f"{number=}, {start_pos=}, {end_pos=}")
            if self._is_activated(start_pos, end_pos, top, bot):
                yield number
            else:
                print("not actived")

    def _is_activated(
        self,
        start_pos: int,
        end_pos: int,
        top: "PartsInfo | None",
        bot: "PartsInfo | None",
    ) -> bool:
        if start_pos in self._active_positions or end_pos in self._active_positions:
            print("activated by the same line")
            return True
        if top and top.activates(start_pos, end_pos):
            print("activated by line above")
            return True
        if bot and bot.activates(start_pos, end_pos):
            print("activated by line below")
            return True
        return False

    def __str__(self) -> str:
        return self._info

    @staticmethod
    def _is_symbol(char: str) -> bool:
        try:
            int(char)
            return False
        except ValueError:
            return char != "."


if __name__ == "__main__":
    with open("03.txt", "r") as f:
        lines = f.readlines()

    parts = [PartsInfo(line.strip()) for line in lines]
    all_numbers: list[int] = []
    for i, parts_info in enumerate(parts):
        top = parts[i - 1] if i != 0 else None
        bot = parts[i + 1] if i != len(parts) - 1 else None
        all_numbers.extend(parts_info.get_active_numbers(top, bot))
    print(sum(all_numbers))
