import random

def create_random_matrix(m, n):
    board = []

    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(0, 1))
        board.append(row)

    return board


def print_board(board, agent_pos=None):
 
    for i in range(len(board)):
        for j in range(len(board[0])):

            if agent_pos == (i, j):
                print("A", end=" ")
            else:
                print(board[i][j], end=" ")

        print()

    print()


def interpret_input(board, agent_pos):
    r, c = agent_pos

    percept = {
        "location": (r, c),
        "status": board[r][c]
    }

    return percept


def rule_match(percept, m, n):
    r, c = percept["location"]
    status = percept["status"]
  
    if status == 1:
        return "SUCK"

    if r % 2 == 0:

        if c < n - 1:
            return "RIGHT"

        elif r < m - 1:
            return "DOWN"

    else:

        if c > 0:
            return "LEFT"

        elif r < m - 1:
            return "DOWN"

    return "NOOP"


def action(board, agent_pos, act):

    r, c = agent_pos

    if act == "SUCK":
        board[r][c] = 0

    elif act == "RIGHT":
        c += 1

    elif act == "LEFT":
        c -= 1

    elif act == "DOWN":
        r += 1

    return (r, c)


def all_clean(board):

    for row in board:
        for cell in row:
            if cell == 1:
                return False

    return True


def simple_reflex_agent(m, n):

    board = create_random_matrix(m, n)
    agent_pos = (0, 0)

    step = 0

    print("Ma trận ban đầu:")
    print_board(board, agent_pos)

    while True:

        percept = interpret_input(board, agent_pos)

        act = rule_match(percept, m, n)

        print("Bước", step + 1)
        print("Percept:", percept)
        print("Action:", act)

        agent_pos = action(board, agent_pos, act)

        print_board(board, agent_pos)

        step += 1

        if act == "NOOP" or all_clean(board):
            break

    print("Đã làm sạch xong!")
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

simple_reflex_agent(m, n)