import copy

def print_world(world):
    print("Location:", world["location"])
    print("A:", world["A"])
    print("B:", world["B"])
    print("----------------")

def all_clean(world):
    return world["A"] == "Clean" and world["B"] == "Clean"


def interpret_input(percept):
    state = {
        "location": percept["location"],
        "current_status": percept[percept["location"]],
        "A": percept["A"],
        "B": percept["B"]
    }
    return state

def rule_match(state, rules):
    location = state["location"]
    current_status = state["current_status"]


    if current_status == "Dirty":
        return {"condition": "dirty", "action": "SUCK"}

    if location == "A":
        return {"condition": "at_A_clean", "action": "RIGHT"}

    if location == "B":
        return {"condition": "at_B_clean", "action": "LEFT"}

    return None


def simple_reflex_agent(percept, rules):
    state = interpret_input(percept)
    rule = rule_match(state, rules)
    if rule is None:
        return "NOOP"
    return rule["action"]

def update_world(world, action):
    new_world = copy.deepcopy(world)

    if action == "SUCK":
        room = new_world["location"]
        new_world[room] = "Clean"

    elif action == "LEFT":
        new_world["location"] = "A"

    elif action == "RIGHT":
        new_world["location"] = "B"

    return new_world

def input_world():
    world = {}

    loc = input("Nhap vi tri agent (A/B): ").strip().upper()
    while loc not in ["A", "B"]:
        loc = input("Chi nhap A hoac B: ").strip().upper()
    world["location"] = loc

    a = input("Trang thai phong A (Dirty/Clean): ").strip().capitalize()
    while a not in ["Dirty", "Clean"]:
        a = input("Chi nhap Dirty hoac Clean cho phong A: ").strip().capitalize()
    world["A"] = a

    b = input("Trang thai phong B (Dirty/Clean): ").strip().capitalize()
    while b not in ["Dirty", "Clean"]:
        b = input("Chi nhap Dirty hoac Clean cho phong B: ").strip().capitalize()
    world["B"] = b

    return world
def main():
    rules = [
        {"condition": "dirty", "action": "SUCK"},
        {"condition": "at_A_clean", "action": "RIGHT"},
        {"condition": "at_B_clean", "action": "LEFT"}
    ]

    world = input_world()

    print("\nTRANG THAI BAN DAU:")
    print_world(world)

    step = 0
    max_steps = 20

    while not all_clean(world) and step < max_steps:
        percept = world
        action = simple_reflex_agent(percept, rules)

        print(f"BUOC {step + 1} - ACTION: {action}")

        world = update_world(world, action)
        print_world(world)

        step += 1

    if all_clean(world):
        print("DA VE TRANG THAI SACH HOAN TOAN!")
    else:
        print("CHUA SACH HOAN TOAN.")

if __name__ == "__main__":
    main()