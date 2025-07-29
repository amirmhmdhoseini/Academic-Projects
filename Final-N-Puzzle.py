import heapq
from collections import deque

# Taarife kelas baraye gereh haye masaleh
class Node:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state  # Vaziate feli puzzle
        self.parent = parent  # Gereh valed
        self.move = move  # Harekati ke be in gereh resid ast
        self.cost = cost  # Hazine baraye residan be in gereh

    def __lt__(self, other):
        # Baraye estefade dar saf olaviat, gereh-ha bayad ghabele moghayese bashand
        return self.cost < other.cost

# Tabe baraye ijade vaziate hadaf bar asase n
def create_goal_state(n):
    return [[(i * n + j + 1) % (n * n) for j in range(n)] for i in range(n)]

# Tabe baraye peyda kardan mokhtasate adade sefr (faza khali)
def find_zero(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

# Tabe baraye tolide harekat haye momken az yek vaziate khas
def get_neighbors(state):
    neighbors = []
    n = len(state)
    zero_x, zero_y = find_zero(state)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Harekat be rast, paiin, chap, bala

    for dx, dy in moves:
        x, y = zero_x + dx, zero_y + dy
        if 0 <= x < n and 0 <= y < n:
            new_state = [row[:] for row in state]
            # Jabejaii adade sefr ba khane hadaf
            new_state[zero_x][zero_y], new_state[x][y] = new_state[x][y], new_state[zero_x][zero_y]
            neighbors.append((new_state, (dx, dy)))

    return neighbors

# Estekhraj masir harekat az gereh hadaf
def extract_solution(node):
    path = []
    while node.parent is not None:
        path.append(node.move)
        node = node.parent
    return path[::-1]

# BFS piade sazi algoritm
def bfs(start_state, goal_state):
    queue = deque([Node(start_state)])
    visited = set()

    while queue:
        node = queue.popleft()
        visited.add(tuple(tuple(row) for row in node.state))

        # Barresi vaziate hadaf
        if node.state == goal_state:
            return extract_solution(node), node.state

        for neighbor, move in get_neighbors(node.state):
            if tuple(tuple(row) for row in neighbor) not in visited:
                queue.append(Node(neighbor, node, move))

    return None, None

# A* piade sazi algoritm
# Tabe arzyabi (hazine + takhmin)
def heuristic(state, goal_state):
    # Majmue fasele haye manhattan baraye har khane
    distance = 0
    n = len(state)
    for i in range(n):
        for j in range(n):
            value = state[i][j]
            if value != 0:
                target_x, target_y = divmod(value - 1, n)
                distance += abs(target_x - i) + abs(target_y - j)
    return distance

def a_star(start_state, goal_state):
    open_set = []
    visited = set()
    heapq.heappush(open_set, (0, Node(start_state)))

    while open_set:
        _, node = heapq.heappop(open_set)
        visited.add(tuple(tuple(row) for row in node.state))

        # Barresi vaziate hadaf
        if node.state == goal_state:
            return extract_solution(node), node.state

        for neighbor, move in get_neighbors(node.state):
            neighbor_tuple = tuple(tuple(row) for row in neighbor)
            if neighbor_tuple not in visited:
                cost = node.cost + 1
                priority = cost + heuristic(neighbor, goal_state)
                heapq.heappush(open_set, (priority, Node(neighbor, node, move, cost)))

    return None, None

# Tabe asli baraye gereftane voroodi va ejra
def main():
    n = int(input("N ra vared konid : "))
    print(f"n = {n}")

    # Gereftane vaziate avalie az karbar
    start_state = []
    print("Vaziat avalie puzzle ra vared konid (satr be satr):")
    for _ in range(n):
        start_state.append(list(map(int, input().split())))

    # Tolide vaziate hadaf bar asase n
    goal_state = create_goal_state(n)

    # Hal kardan puzzle ba estefade az BFS
    print("\nHal ba estefade az BFS:")
    bfs_solution, bfs_final_state = bfs(start_state, goal_state)
    if bfs_solution:
        print("Puzzle qabel hal ast.")
        print("Masir hal (BFS):\n", bfs_solution)
        print("Vaziat nahai:")
        for row in bfs_final_state:
            print(row)
    else:
        print("Puzzle qabel hal nist.")

    # Hal kardan puzzle ba estefade az A*
    print("\nHal ba estefade az A*:")
    a_star_solution, a_star_final_state = a_star(start_state, goal_state)
    if a_star_solution:
        print("Puzzle qabel hal ast.")
        print("Masir hal (A*):\n", a_star_solution)
        print("Vaziat nahai:")
        for row in a_star_final_state:
            print(row)
    else:
        print("Puzzle qabel hal nist.")

if __name__ == "__main__":
    main()
