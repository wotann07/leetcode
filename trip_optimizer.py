class TripOptimizer:

    @staticmethod
    def get_optimal_routes(max_distance: int, dest: [], ret: []):
        optimal_d = 0
        optimal_routes = []
        for d in dest:
            for r in ret:
                total_d = d[1] + r[1]
                if total_d <= max_distance:
                    if total_d >= optimal_d:
                        if total_d > optimal_d:
                            optimal_routes.clear()
                            optimal_d = total_d
                        optimal_routes.append([d[0], r[0]])

        return optimal_routes
