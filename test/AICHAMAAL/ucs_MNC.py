from queue import PriorityQueue


def is_valid(state):
    m_left, c_left, b_pos, m_right, c_right = state
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 3 or c_left > 3 or m_right > 3 or c_right > 3:
        return False
    if (c_left > m_left > 0) or (c_right > m_right > 0):
        return False
    return True


def next_states(state):
    m_left, c_left, b_pos, m_right, c_right = state
    if b_pos == "left":
        moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
        # This is basically 2 Ms 0 Cs -> So it represents boat mai kitne log aur kon kon jaah raha hai
        next_states = [(m_left-m, c_left-c, 'right', m_right+m, c_right+c)
                       for m, c in moves]

    else:
        moves = [(-2, 0), (0, -2), (-1, -1), (-1, 0), (0, -1)]
        next_states = [(m_left+m, c_left+c, 'left', m_right-m, c_right-c)
                       for m, c in moves]

    return [state for state in next_states if is_valid(state)]


def ucs(start_state):
    frontier=PriorityQueue()
    frontier.put((0,[start_state]))
    explored=set()

    while not frontier.empty():
        cost,path=frontier.get()
        current_state=path[-1]
        if current_state==(0,0,"right",3,3):
            return path
        for next_state in next_states(current_state):
            if next_state not in explored:
                new_cost=cost+1
                new_path=path+[next_state]
                frontier.put((new_cost,new_path))
                explored.add(next_state)



start_state=(3,3,'left',0,0)
path=ucs(start_state)

for state in path:
    m_left, c_left, b_pos, m_right, c_right = state
    print(f"{m_left} missionaries and {c_left} cannibals on the left side, {m_right} missionaries and {c_right} cannibals on the right side \nBoat on {b_pos} side\n")
