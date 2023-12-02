# COMPLETED


class City:
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def __repr__(self):
        return f"<City {self.name}>"

    def add_connection(self, city, distance):
        self.connections[city] = distance
    
def print_route(route, route_length):
    acumulated_distance = 0
    connection_distance = 0
    for city in route:
        if city == route[-1]:
            print(city.name)
        else:
            connection_distance = city.connections[route[route.index(city)+1]]
            acumulated_distance += city.connections[route[route.index(city)+1]]
            print(city.name, end=f" -[{connection_distance}/{acumulated_distance}]-> ")
    print(f"Total length: {route_length}")

def deep_search(cities, start_city, search_shortest=True):
    visited_cities = []
    not_visited_cities = list(cities.values())

    visited_cities.append(start_city)
    not_visited_cities.remove(start_city)

    route = [start_city]
    route_length = 0

    while len(not_visited_cities) > 0:
        current_city = route[-1]
        next_city = None

        # We iterate over all the connections of the current city
        # Next city is the one with the shortest distance (heuristic of part on)
        for city, distance in current_city.connections.items():
            if city not in visited_cities:
                if next_city is None:
                    next_city = city
                else:
                    if search_shortest:
                        if distance < current_city.connections[next_city]:
                            next_city = city
                    else: # Search longest for part two
                        if distance > current_city.connections[next_city]:
                            next_city = city
    
        # We add the next city to the route
        route.append(next_city)
        route_length += current_city.connections[next_city]
        
        # We update the visited cities
        visited_cities.append(next_city)
        not_visited_cities.remove(next_city)

    return route, route_length



if __name__ == "__main__":
    with open("input") as f:
        distances = f.readlines()

    # Parse information
    cities = {}
    for distance in distances:
        distance = distance.strip().split(" ")
        city1 = distance[0]
        city2 = distance[2]
        distance = int(distance[4])

        if city1 not in cities:
            cities[city1] = City(city1)
        if city2 not in cities:
            cities[city2] = City(city2)

        cities[city1].add_connection(cities[city2], distance)
        cities[city2].add_connection(cities[city1], distance)
    
    # Cities:
    # Faerun, Tristram, Tambi, Norrath, Snowdin, Straylight, AlphaCentauri, Arbre
    print("CITIES:")
    print(list(cities.values()))
    
    print("-"*50)

    print("PART ONE:")
    min_route = []
    min_route_length = 99999999
    for city in cities.values():
        route, route_length = deep_search(cities, city)
        if route_length < min_route_length:
            min_route = route
            min_route_length = route_length
    print("Shortest route for all cities:")
    print_route(min_route, min_route_length)

    print("-"*50)

    print("PART TWO:")
    max_route = []
    max_route_length = 0
    for city in cities.values():
        route, route_length = deep_search(cities, city, search_shortest=False)
        if route_length > max_route_length:
            max_route = route
            max_route_length = route_length
    print("Longest route for all cities:")
    print_route(max_route, max_route_length)


    