class XNearestSteakHouses:

    @staticmethod
    def __get_distance(point: []):
        return (point[0] ** 2 + point[1] ** 2) ** 0.5

    @staticmethod
    def get_x_nearest_steakhouses(all_locations: [], x: int):
        return list(sorted(all_locations, key=lambda point: XNearestSteakHouses.__get_distance(point)))[:x]
