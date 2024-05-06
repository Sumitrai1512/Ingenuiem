import random


def generate_random_board(n):
    """ 
    Generate a random board configuration.
    
    Args:
    n (int): Size of the chessboard and number of queens.
    
    Returns:
    list: A list representing the board configuration, where each index represents a row 
          and the value at that index represents the column where the queen is placed.
    """
    board = list(range(n))  # Create a list representing columns
    random.shuffle(board)    # Shuffle the list to generate a random board
    return board


def count_attacking_pairs(board):
    """ 
    Count the number of attacking pairs of queens.
    
    Args:
    board (list): A list representing the board configuration.
    
    Returns:
    int: The number of pairs of queens that are attacking each other.
    """
    n = len(board)
    count = 0

    # Check all pairs of queens
    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[j] - board[i]) == j - i:
                count += 1  # Found an attacking pair

    return count


def hill_climbing(n, max_iterations=000):
    """ 
    Use hill climbing algorithm to solve the N-Queens problem.
    
    Args:
    n (int): Size of the chessboard and number of queens.
    max_iterations (int): Maximum number of iterations for the algorithm (default is 1000).
    
    Returns:
    list or None: A board configuration if a solution is found, otherwise None.
    """
    # Initialize with a random board
    current_board = generate_random_board(n)
    current_attacks = count_attacking_pairs(current_board)

    for _ in range(max_iterations):
        if current_attacks == 0:
            return current_board  # Solution found

        # Explore neighbors to find a better solution
        best_board = current_board
        best_attacks = current_attacks

        for i in range(n):
            for j in range(i + 1, n):
                # Swap two queens and count the attacks
                next_board = current_board[:]
                next_board[i], next_board[j] = next_board[j], next_board[i]
                next_attacks = count_attacking_pairs(next_board)

                # Check if the new board is better
                if next_attacks < best_attacks:
                    best_board = next_board
                    best_attacks = next_attacks

        # Check if we reached a local minimum
        if best_attacks >= current_attacks:
            break  # No better solution found

        # Move to the better solution
        current_board = best_board
        current_attacks = best_attacks

    return None  # No solution found within the maximum iterations


def print_board(board):
    """ 
    Print the board configuration.
    
    Args:
    board (list): A list representing the board configuration.
    """
    n = len(board)
    for row in range(n):
        line = ['Q' if i == board[row] else '.' for i in range(n)]
        print(' '.join(line))


if __name__ == '__main__':
    n = 8  # Size of the chessboard (N-Queens problem)
    max_iterations = 5000  # Increase the maximum number of iterations

    # Use hill climbing to find a solution
    solution = hill_climbing(n, max_iterations=max_iterations)

    if solution is not None:
        print("Solution found:")
        print_board(solution)
    else:
        print("No solution found within the maximum iterations.")
