class VacuumAgent:
    
"""
    A simple Reflex Vacuum Agent that follows a set of rules:
    1. If the current location is dirty, Suck.
    2. If the current location is clean, move to the other location.
"""
    
    def __init__(self):
        
    #Environment state: 1 represents 'Dirty', 0 represents 'Clean'
    # In a real scenario, this state would be external to the agent.
        
        self.environment_status = {'A': 1, 'B': 1} 
        
        # Internal state: The agent's current physical position
        self.current_location = 'A'

    def run_cleaning_cycle(self):
        
  
        #Simulates the agent's decision-making process over a fixed period.
    
        print(f"--- Starting Cleaning Task at Location {self.current_location} ---")
        
        #We loop through the number of locations to ensure the agent visits all spots
        
        for step in range(len(self.environment_status)):
            
            #PERCEIVE: The agent senses the state of its current square
            is_dirty = self.environment_status[self.current_location] == 1
            
            print(f"[Sensor] Location {self.current_location} status: "
                  f"{'DIRTY' if is_dirty else 'CLEAN'}")

            #DECIDE & ACT: Rule-based behavior
            if is_dirty:
                # Condition-Action Rule: If Dirty then Suck
                print(f"[Action] Sucking dirt at {self.current_location}...")
                self.environment_status[self.current_location] = 0 # Update environment
                print(f"[Success] {self.current_location} is now clean.")
            else:
                # Condition-Action Rule: If Clean then No-Op (or move)
                print(f"[Action] {self.current_location} is already clean. No cleaning needed.")

            #MOVE: The agent changes its location to explore the environment
            old_location = self.current_location
            self.current_location = 'B' if self.current_location == 'A' else 'A'
            
            #Avoid printing a move message after the final step
            if step < len(self.environment_status) - 1:
                print(f"[Movement] Moving from {old_location} to {self.current_location}.\n")

        print("\n--- Task Complete: All locations processed. ---")

#Program Execution 
if __name__ == "__main__":
    #Instantiate the agent
    my_vacuum = VacuumAgent()
    
    #Execute the cleaning logic
    my_vacuum.run_cleaning_cycle()
