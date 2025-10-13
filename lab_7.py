class RouteMap:
    def __init__(self, routes):
        self.routes = routes

    def adjacent_nodes(self, point):
        return self.routes.get(point, [])

    # Estimated remaining distance (heuristic)
    def estimated_cost(self, point):
        estimates = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }
        return estimates.get(point, float('inf'))

    def a_star_search(self, source, target):
        to_visit = [source]
        visited = []

        # Record shortest distance from source
        path_cost = {source: 0}

        # Track the path
        previous = {source: None}

        while to_visit:
            # Choose node with smallest f = g + h
            best = min(to_visit, key=lambda node: path_cost[node] + self.estimated_cost(node))

            # Goal found → backtrack path
            if best == target:
                route = []
                while best is not None:
                    route.append(best)
                    best = previous[best]
                route.reverse()
                print("Shortest Path:", route)
                return route

            to_visit.remove(best)
            visited.append(best)

            # Explore each connected node
            for (adjacent, weight) in self.adjacent_nodes(best):
                new_cost = path_cost[best] + weight
                if adjacent not in path_cost or new_cost < path_cost[adjacent]:
                    path_cost[adjacent] = new_cost
                    previous[adjacent] = best
                    if adjacent not in visited:
                        to_visit.append(adjacent)

        print("No valid route found!")
        return None


# Example usage
routes = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

map_graph = RouteMap(routes)
map_graph.a_star_search('A', 'D')
