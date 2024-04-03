# class State:
#     def __init__(self, missionaries, cannibals, boat_position):
#         self.missionaries = missionaries
#         self.cannibals = cannibals
#         self.boat_position = boat_position

#     def is_valid(self):
#         # Check if the number of missionaries is greater than or equal to the number of cannibals
#         # on both sides of the river, and neither side has negative numbers of missionaries or cannibals
#         if self.missionaries < 0 or self.missionaries > 3 or self.cannibals < 0 or self.cannibals > 3:
#             return False
#         if self.missionaries < self.cannibals and self.missionaries > 0:
#             return False
#         # if 3 - self.missionaries < 3 - self.cannibals and 3 - self.missionaries > 0:
#         #     return False
#         return True

#     def is_goal(self):
#         # return self.missionaries == 0 and self.cannibals == 0 and self.boat_position == 0
#          return self.missionaries == 0 and self.cannibals == 0 

#     def __str__(self):
#         return f'Missionaries: {self.missionaries}, Cannibals: {self.cannibals}, Boat Position: {"Left" if self.boat_position == 0 else "Right"}'

# class Node:
#     def __init__(self, state, parent=None, action=None):
#         self.state = state
#         self.parent = parent
#         self.action = action

#     def expand(self):
#         children = []
#         moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

#         for move in moves:
#             new_state = State(self.state.missionaries + move[0] if self.state.boat_position == 0 else self.state.missionaries - move[0],
#                               self.state.cannibals + move[1] if self.state.boat_position == 0 else self.state.cannibals - move[1],
#                               1 if self.state.boat_position == 0 else 0)

#             if new_state.is_valid():
#                 children.append(Node(new_state, self, move))
#         return children

#     def print_solution(self):
#         path = []
#         node = self
#         while node:
#             path.append((node.state, node.action))
#             node = node.parent
#         path.reverse()
#         for state, action in path:
#             print(state)
#             if action:
#                 print(f'Move {action[0]} missionaries and {action[1]} cannibals {"from left to right" if state.boat_position == 0 else "from right to left"}')

# def breadth_first_search(initial_state):
#     start_node = Node(initial_state)
#     if start_node.state.is_goal():
#         return start_node

#     frontier = [start_node]
#     explored = set()

#     while frontier:
#         node = frontier.pop(0)
#         explored.add(node.state)

#         for child in node.expand():
#             if child.state not in explored:
#                 if child.state.is_goal():
#                     return child
#                 frontier.append(child)
#     return None

# def main():
#     initial_state = State(3, 3, 0)
#     solution = breadth_first_search(initial_state)
#     if solution:
#         print("Solution found:")
#         solution.print_solution()
#     else:
#         print("No solution found.")

# if __name__ == "__main__":
#     main()



from collections import deque

class State:
    def __init__(self, mleft, cleft, mright, cright, boat):
        self.mleft = mleft
        self.cleft = cleft
        self.mright = mright
        self.cright = cright
        self.boat = boat
    
    def is_valid(self):
        if self.mleft < 0 or self.cleft < 0 or self.mright < 0 or self.cright < 0:
            return False
        if (self.mleft > 0 and self.cleft > self.mleft) or (self.mright > 0 and self.cright > self.mright):
            return False
        return True
  
    def is_goal(self):
        return self.mleft == 0 and self.cleft == 0

def getNextMoves(state):
    moves = []
    if state.boat == 1:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = State(state.mleft - m, state.cleft - c, state.mright + m, state.cright + c, 2)
                    if new_state.is_valid():
                        moves.append(new_state)
    else:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = State(state.mleft + m, state.cleft + c, state.mright - m, state.cright - c, 1)
                    if new_state.is_valid():
                        moves.append(new_state)
    return moves

def bfs(initial_state):
    visited = set()
    queue = deque([([initial_state], initial_state)])
    
    while queue:
        path, current_state = queue.popleft()
        visited.add((current_state.mleft, current_state.cleft, current_state.mright, current_state.cright, current_state.boat))
        
        if current_state.is_goal():
            return path
        
        for next_state in getNextMoves(current_state):
            if (next_state.mleft, next_state.cleft, next_state.mright, next_state.cright, next_state.boat) not in visited:
                new_path = path + [next_state]
                queue.append((new_path, next_state))
                visited.add((next_state.mleft, next_state.cleft, next_state.mright, next_state.cright, next_state.boat))
    return None

def printPath(path):
    for s in path:
        print(s.mleft, s.cleft, s.mright, s.cright, s.boat)

# Define initial state
initial_state = State(3, 3, 0, 0, 1)

# Solve using BFS
solution = bfs(initial_state)

# Print solution path
if solution:
    print("Solution found:")
    printPath(solution)
else:
    print("No solution exists.")

