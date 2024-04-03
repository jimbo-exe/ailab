#for best first, use visited and dont use H(n). only use g(n).
#for A*, no need for visited path.

import heapq

def calcost(path,distances):
    c=0
    for i in range(len(path)-1):
       c=c+distances[cities.index(path[i])][cities.index(path[i+1])]
    return c

def astar(start_city, cities, distances):
    num_cities = len(cities)
    visited = set()
    pq = [(0, start_city, [start_city])] # (cost, current_city, path)
    
    while pq:
        print("PQ:", pq)
        c, current_city, path = heapq.heappop(pq)
        print("Current city:", current_city)
        print("Path:", path)
        
        if len(path) == num_cities: # if all cities are visited
            new_path = path + [cities[0]]
            i=cities.index(path[-1]) # last city
            # print (i)
            c=c+distances[i][0]
            pro = calcost(new_path,distances) # value of g(n)
            return new_path,c,pro
        
        visited.add(tuple(path))
        
        # l1 = [x for x in cities if x not in path]
        for next_city in [x for x in cities if x not in path]: #l1 is the list of cities not in path
            # if next_city not in path:
            new_path = path + [next_city] #
            if tuple(new_path) not in visited:
                p= calcost(new_path,distances)+heuristic[cities.index(next_city)] #a* heuristic function f(n)=g(n)+h(n)
                heapq.heappush(pq, (p, next_city, new_path))
    
    return None,0,0

# Example usage
cities = ['A', 'B', 'C', 'D']  # Example cities

distances = [
    [0, 50, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]  # Example distances between cities

heuristic=[90,80,70,60]
start_city = cities[0]
path,cost,pro = astar(start_city, cities, distances) # cost = with heuristic, pro = without heuristic
print(path,cost,pro)