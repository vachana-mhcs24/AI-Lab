import random

N = 4

def cost(board):
    """Count pairs of queens attacking each other."""
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (board[i] == board[j] or
                abs(board[i] - board[j]) == abs(i - j)):
                conflicts += 1
    return conflicts


def get_neighbors(board):
    """Move one queen to another row in its column (0-indexed: rows 0 to N-1)."""
    neighbors = []
    for col in range(N):
        for row in range(N):
            if row != board[col]:
                neighbor = board.copy()
                neighbor[col] = row
                neighbors.append((col, row, neighbor))
    return neighbors


def print_grid(board):
    """Print the N-Queens solution as an N x N grid."""
    print("\nGrid Representation:")
    for row in range(N):
        line = ["Q" if board[col] == row else "." for col in range(N)]
        print(" ".join(line))


def hill_climbing(initial_state=None):
    restart = 0

    while True:
        restart += 1
        # Use initial_state for the first attempt, then random boards for restarts
        if restart == 1 and initial_state is not None:
            current = initial_state.copy()
        else:
            current = [random.randint(0, N - 1) for _ in range(N)]

        print(f"\nRestart {restart}: Initial state = {current}")
        print("Initial cost =", cost(current))

        while True:
            current_cost = cost(current)

            if current_cost == 0:
                print("\nGOAL FOUND!")
                print("Final board:", current)
                print("Final cost:", current_cost)
                print_grid(current)
                return current

            neighbors = get_neighbors(current)

            print("\nCurrent state:", current)
            print("Current cost:", current_cost)
            print("Neighbor states and costs:")

            for col, row, neighbor in neighbors:
                print(
                    f" Move column {col} to row {row}: "
                    f"{neighbor}, cost = {cost(neighbor)}"
                )

            # Choose a minimum-cost neighbor.
            best_cost = min(cost(nb) for _, _, nb in neighbors)
            best_neighbors = [
                nb for _, _, nb in neighbors
                if cost(nb) == best_cost
            ]
            best = random.choice(best_neighbors)

            # Restart if no improvement is possible.
            if best_cost >= current_cost:
                print("Local minimum reached; restarting...")
                break

            current = best


if __name__ == "__main__":
    hill_climbing(initial_state=[3, 1, 2, 0])