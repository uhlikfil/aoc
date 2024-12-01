import functools


class Draw:
    def __init__(self, draw: str) -> None:
        self.cubes: dict[str, int] = {}
        for cube_info in draw.split(", "):
            count, color = cube_info.split(" ")
            self.cubes[color] = int(count)

    def is_feasible(self, available_cubes: dict[str, int]) -> bool:
        for color, count in self.cubes.items():
            if available_cubes[color] < count:
                return False
        return True


class Game:
    def __init__(self, line: str) -> None:
        game, draws = line.split(":")
        _, num = game.split(" ")
        self._id = int(num.strip())
        self._draws = [Draw(draw.strip()) for draw in draws.split(";")]

    def feasibility_score(self, available_cubes: dict[str, int]) -> int:
        return (
            int(self._id)
            if all(draw.is_feasible(available_cubes) for draw in self._draws)
            else 0
        )

    def get_min_feasible_power(self) -> int:
        min_available_cubes = {"red": 0, "green": 0, "blue": 0}
        for draw in self._draws:
            for color, count in draw.cubes.items():
                min_available_cubes[color] = max(min_available_cubes[color], count)
        return functools.reduce(lambda x, y: x * y, min_available_cubes.values())


if __name__ == "__main__":
    available_cubes = {"red": 12, "green": 13, "blue": 14}
    with open("02.txt", "r") as f:
        lines = f.readlines()
    games = [Game(game) for game in lines]

    feasibility_score = sum(game.feasibility_score(available_cubes) for game in games)
    power = sum(game.get_min_feasible_power() for game in games)
    print(feasibility_score)
    print(power)
