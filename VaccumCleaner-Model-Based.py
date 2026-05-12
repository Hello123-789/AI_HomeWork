import random

def create_random_matrix(m, n):
    return [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]

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
    return {
        "location": (r, c),
        "status": board[r][c]  
    }

def init_state(m, n):
    
    return {
        "position": (0, 0),
        "direction": "RIGHT",              
        "last_action": None,
        "visited": set(),
        "internal_map": [[-1 for _ in range(n)] for _ in range(m)]
        
    }

def update_state(state, percept):
   
    r, c = state["position"]
    state["internal_map"][r][c] = percept["status"]
    state["visited"].add((r, c))
    return state

def rule_match(state, m, n):
    
    r, c = state["position"]
    status = state["internal_map"][r][c]

    if status == 1:
        return "SUCK"

    if state["direction"] == "RIGHT":
        if c < n - 1:
            return "RIGHT"
        elif r < m - 1:
            return "DOWN"
        else:
            return "NOOP"

    else:  
        if c > 0:
            return "LEFT"
        elif r < m - 1:
            return "DOWN"
        else:
            return "NOOP"

def action(board, state, act):
    
    r, c = state["position"]

    if act == "SUCK":
        board[r][c] = 0

    elif act == "RIGHT":
        c += 1

    elif act == "LEFT":
        c -= 1

    elif act == "DOWN":
        r += 1
        state["direction"] = "LEFT" if state["direction"] == "RIGHT" else "RIGHT"

    state["position"] = (r, c)
    state["last_action"] = act
    return state

def all_clean(board):
    for row in board:
        for cell in row:
            if cell == 1:
                return False
    return True

def model_based_reflex_agent(m, n):
    board = create_random_matrix(m, n)
    state = init_state(m, n)
    step = 0

    print("Ma trận ban đầu:")
    print_board(board, state["position"])

    while True:
        percept = interpret_input(board, state["position"])

        state = update_state(state, percept)

        act = rule_match(state, m, n)

        print(f"Bước {step + 1}: percept={percept}, action={act}")

        if act == "NOOP":
            break
        state = action(board, state, act)

        print_board(board, state["position"])
        step += 1

        if all_clean(board):
            print("Đã làm sạch xong!")
            print_board(board, state["position"])
            break

m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

model_based_reflex_agent(m, n)