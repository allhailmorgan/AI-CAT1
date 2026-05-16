
#GRAPH DEFINITION

#Using the identical graph structure to showcase structural differences.
# 
#        A (Start)
#       / \
#      B   C
#     / \   \
#    D   E   F
#         \
#          G (Goal)
#
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

def depth_first_search(graph, start, goal):
    """
    Performs DFS to find a path from start to goal.
    Uses a LIFO stack to explore deep into branches before backtracking.
    """
    #Initialize the stack with a tuple containing: (current_node, path_taken_so_far)
    
    #A standard Python list acts perfectly as a stack using .append() and .pop()
    
    stack = [(start, [start])]
    
    #Track visited nodes to prevent cyclic redundancy
    
    visited = set()
    
    print("--- DFS Traversal Steps ---")
    
    while stack:
        #Pop the last element added to the list (Last-In, First-Out)
        
        current_node, path = stack.pop()
        print(f"Visiting Node: {current_node} | Current Path: {' -> '.join(path)}")
        
        #Check if we have reached our target destination
        
        if current_node == goal:
            print("\nGoal state reached successfully!")
            return path
            
        #Process the node if it hasn't been visited yet
        
        if current_node not in visited:
            visited.add(current_node)
            
            #We reverse the neighbors list here solely to maintain a standard left-to-right 
            
            #evaluation order when popping from a LIFO stack.
            
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    # Construct the updated path tracking
                    new_path = path + [neighbor]
                    # Push onto the top of the stack
                    stack.append((neighbor, new_path))
                    
    print("\nGoal state could not be reached.")
    return None

#Execution of program
if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'G'
    
    result_path = depth_first_search(graph, start_node, goal_node)
    
    print("\n==============================================")
    print(f"FINAL DFS PATH: {' -> '.join(result_path) if result_path else 'No path found'}")
    print("==============================================")
