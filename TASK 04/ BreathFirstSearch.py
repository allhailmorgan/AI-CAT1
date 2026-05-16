
from collections import deque

# GRAPH DEFINITION

# The graph is represented as an adjacency list.
# 
#        A        (Start)
#       / \
#      B   C
#     / \   \
#    D   E   F
#         \
#          G      (Goal)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

def breadth_first_search(graph, start, goal):
    """
    Performs BFS to find the shortest path from start to goal in an unweighted graph.
    Uses a FIFO queue to explore nodes level by level.
    """
    #Initialize the queue with a tuple containing: (current_node, path_taken_so_far)
    #We start at the ''start'' node and the path only contains the ''start'' node.
   
  queue = deque([(start, [start])])
    
    #Track visited nodes to prevent infinite loops in graphs with cycles
    visited = set()
    
    print("--- BFS Traversal Steps ---")
    
    while queue:
        #Pop the most left element (First-In, First-Out)
      
        current_node, path = queue.popleft()
        print(f"Visiting Node: {current_node} | Current Path: {' -> '.join(path)}")
        
        #Check if we have reached our target destination
      
        if current_node == goal:
            print("\nGoal state reached successfully!")
            return path
            
        #Process the node if it hasn't been visited yet
        if current_node not in visited:
            visited.add(current_node)
            
            #Fetch all unvisited neighboring nodes
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                  
                    #Construct the updated path including this neighbor
                  
                    new_path = path + [neighbor]
                  
                    #Append to the right side of the queue to ensure layer-by-layer tracking
                    queue.append((neighbor, new_path))
                    
    print("\nGoal state could not be reached.")
    return None

#Execution of program
if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'G'
    
    result_path = breadth_first_search(graph, start_node, goal_node)
    
    print("\n==============================================")
    print(f"FINAL BFS PATH: {' -> '.join(result_path) if result_path else 'No path found'}")
    print("==============================================")
