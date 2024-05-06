import collections

def bfs(num_disks,source,target,auxiliary):
    #INITIALISATION PART

    initial_state = (tuple(range(num_disks, 0, -1)), (), ())

    def state_key(state):
        #This will output ((A,),(B,),(C,)) because for each iteration of the for loop it will get (A,)
        return tuple(tuple(peg) for peg in state)
    
    #Basically will hold tuples of (Initial State,list of moves)
    queue=collections.deque([(initial_state,[])])

    #Create a set to store univisited states
    visited=set()
    visited.add(state_key(initial_state))

    while queue:
        current_state,moves=queue.popleft()

        #Check if final state is achieved (ALL DISKS ON TARGET PEG)
        # pegs.index(target) -> Pegs ke andar joh index pe target hai USKA INDEX DE
        if current_state[pegs.index(target)] == tuple(range(num_disks,0,-1)):
            return moves
        
        for i in range(3):
            if not current_state[i]:
                continue
            for j in range(3):
                if i ==j:
                    continue
                if current_state[j] and current_state [j][-1]<current_state[i][-1]:
                    continue
                new_state=[list(peg) for peg in current_state]
                disk = new_state[i].pop()
                new_state[j].append(disk)
                new_state = tuple(tuple(peg) for peg in new_state)

                if state_key(new_state) not in visited:
                    #Add this new state to visited
                    visited.add(state_key(new_state))
                    new_moves = moves + [f"Move disk {disk} from {pegs[i]} to {pegs[j]}"]
                    queue.append((new_state, new_moves))
    return None


if __name__=="__main__":
    num_disks=int(input("Enter the Number of Disks: "))
    source, target, auxiliary = "A", "B", "C"
    pegs = (source, auxiliary, target)  # Peg order for convenience
    solution = bfs(num_disks, source, target, auxiliary)
    if solution:
        for step, move in enumerate(solution):
            print(f"Step {step + 1}: {move}")
    else:
        print("No solution found.")

