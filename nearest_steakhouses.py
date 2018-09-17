from operator import itemgetter


class XNearestSteakHouses:

    @staticmethod
    def __get_distance(point: []):
        return (point[0] ** 2 + point[1] ** 2) ** 0.5

    @staticmethod
    def get_x_nearest_steakhouses(all_locations: [], x: int):
        for point in all_locations:
            point.append(XNearestSteakHouses.__get_distance(point))

        return list(map(lambda loc: loc[:2], list(sorted(all_locations, key=itemgetter(2)))[:x]))
