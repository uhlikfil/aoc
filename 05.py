class Translation:
    def __init__(self, translation_def: str) -> None:
        self.dst_start, self.src_start, size = (int(n) for n in translation_def.split())
        self.src_end = self.src_start + size

    def translate(self, source: int) -> int | None:
        if source < self.src_start or source > self.src_end:
            return None
        diff_from_start = source - self.src_start
        return self.dst_start + diff_from_start


class Map:
    def __init__(self, map_definition: list[str]) -> None:
        self._translations = [Translation(d) for d in map_definition]

    def get_destination(self, source: int) -> int:
        for translation in self._translations:
            destination = translation.translate(source)
            if destination is not None:
                return destination
        return source


def traverse_maps(start: int, maps: list[Map]) -> int:
    result = start
    for map in maps:
        result = map.get_destination(result)
    return result


def get_lowest_seed_location(seeds: list[int], maps: list[Map]) -> int:
    locations = (traverse_maps(seed, maps) for seed in seeds)
    return min(locations)


if __name__ == "__main__":
    with open("05.txt", "r") as f:
        raw_almanac = f.read()

    seeds_def, *map_defs = raw_almanac.split("\n\n")
    seeds = [int(n) for n in seeds_def[6:].split()]
    maps = []
    for map_def in map_defs:
        maps.append(Map(map_def.strip().split("\n")[1:]))

    print(get_lowest_seed_location(seeds, maps))
