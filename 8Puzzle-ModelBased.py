import copy
import random

GOAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def print_board(board):

    for row in board:
        for x in row:
            print(x, end=" ")
        print()

    print("----------------")

def find_zero(board):

    for i in range(3):
        for j in range(3):

            if board[i][j] == 0:
                return i, j
def is_goal(board):
    return board == GOAL
def move(board, direction):

    new_board = copy.deepcopy(board)

    x, y = find_zero(new_board)

    if direction == "UP" and x > 0:
        new_board[x][y], new_board[x - 1][y] = new_board[x - 1][y], new_board[x][y]
        return new_board

    if direction == "DOWN" and x < 2:
        new_board[x][y], new_board[x + 1][y] = new_board[x + 1][y], new_board[x][y]
        return new_board

    if direction == "LEFT" and y > 0:
        new_board[x][y], new_board[x][y - 1] = new_board[x][y - 1], new_board[x][y]
        return new_board

    if direction == "RIGHT" and y < 2:
        new_board[x][y], new_board[x][y + 1] = new_board[x][y + 1], new_board[x][y]
        return new_board

    return None

def get_legal_moves(board):

    x, y = find_zero(board)

    moves = []

    if x > 0:
        moves.append("UP")

    if x < 2:
        moves.append("DOWN")

    if y > 0:
        moves.append("LEFT")

    if y < 2:
        moves.append("RIGHT")

    return moves

def update_state(state, percept):

    state["board"] = percept
    state["zero_pos"] = find_zero(percept)
    state["legal_moves"] = get_legal_moves(percept)

    state["visited"].append(copy.deepcopy(percept))

    return state

def count_wrong_tiles(board):

    wrong = 0

    for i in range(3):
        for j in range(3):

            if board[i][j] != 0 and board[i][j] != GOAL[i][j]:
                wrong += 1

    return wrong

def rule_match(state, rules):

    board = state["board"]
    legal_moves = state["legal_moves"]
    visited = state["visited"]

    best_rule = None
    best_score = 999999

    for rule in rules:

        action = rule["action"]

        if action in legal_moves:

            next_board = move(board, action)

            if next_board is not None:

                if next_board in visited:
                    continue

                score = count_wrong_tiles(next_board)

                if score < best_score:
                    best_score = score
                    best_rule = rule

    return best_rule

def model_based_reflex_agent(percept, state, rules):

    # UPDATE STATE
    state = update_state(state, percept)

    # RULE MATCH
    rule = rule_match(state, rules)

    if rule is None:
        return None

    return rule["action"]

def create_random_solvable_board(steps=20):

    board = copy.deepcopy(GOAL)

    for _ in range(steps):

        legal_moves = get_legal_moves(board)

        action = random.choice(legal_moves)

        board = move(board, action)

    return board
def main():

    rules = [
        {"condition": "move_up", "action": "UP"},
        {"condition": "move_down", "action": "DOWN"},
        {"condition": "move_left", "action": "LEFT"},
        {"condition": "move_right", "action": "RIGHT"}
    ]

    board = create_random_solvable_board(steps=15)
    state = {
        "board": board,
        "zero_pos": find_zero(board),
        "legal_moves": get_legal_moves(board),
        "visited": []
    }

    print("MA TRAN BAN DAU:")
    print_board(board)

    step = 0
    max_steps = 50

    while not is_goal(board) and step < max_steps:

        action = model_based_reflex_agent(board, state, rules)

        if action is None:
            print("KHONG TIM DUOC HANH DONG TOT HON")
            break

        next_board = move(board, action)

        if next_board is None:
            print("NUOC DI KHONG HOP LE")
            break

        board = next_board

        step += 1

        print(f"BUOC {step} - ACTION: {action}")
        print_board(board)

    if is_goal(board):
        print("DA DAT TRANG THAI DICH!")
    else:
        print("CHUA DAT TRANG THAI DICH!")

if __name__ == "__main__":
    main()