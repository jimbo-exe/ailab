from collections import deque

class WaterJugState:
    def __init__(self, jug1, jug2, parent=None):
        self.jug1 = jug1
        self.jug2 = jug2
        self.parent = parent

    def is_goal_state(self, target):
        return self.jug1 == target[0] and self.jug2 == target[1]

    def get_successors(self, capacities):
        successors = []

        # Filling jug 1
        successors.append(WaterJugState(capacities[0], self.jug2, parent=self))

        # Filling jug 2
        successors.append(WaterJugState(self.jug1, capacities[1], parent=self))

        # Emptying jug 1
        successors.append(WaterJugState(0, self.jug2, parent=self))

        # Emptying jug 2
        successors.append(WaterJugState(self.jug1, 0, parent=self))

        # Pouring from jug 1 to jug 2
        pour_amount = min(self.jug1, capacities[1] - self.jug2)
        successors.append(WaterJugState(self.jug1 - pour_amount, self.jug2 + pour_amount, parent=self))

        # Pouring from jug 2 to jug 1
        pour_amount = min(self.jug2, capacities[0] - self.jug1)
        successors.append(WaterJugState(self.jug1 + pour_amount, self.jug2 - pour_amount, parent=self))

        return successors

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

def bfs_search(start_state, target):
    capacities = (5, 4)  # Capacities of jug 1 and jug 2
    visited = set()
    queue = deque([start_state])

    while queue:
        current_state = queue.popleft()
        visited.add(current_state)

        if current_state.is_goal_state(target):
            return current_state

        successors = current_state.get_successors(capacities)
        for successor in successors:
            if successor not in visited:
                queue.append(successor)
                visited.add(successor)

    return None

def print_solution(solution):
    if solution:
        path = []
        while solution:
            path.append((solution.jug1, solution.jug2))
            solution = solution.parent
        path.reverse()
        print("Solution Path:")
        for state in path:
            print(state)
    else:
        print("No solution found.")

def main():
    initial_state = WaterJugState(0, 0)
    target_state = (0, 3)
    solution = bfs_search(initial_state, target_state)
    print_solution(solution)

main()