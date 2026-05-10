class VacuumAgent:
    def __init__(self):
        # Initializing world: 0 is clean, 1 is dirty
        self.locations = {'A': 1, 'B': 1}
        self.current_pos = 'A'

    def sense_and_act(self):
        for _ in range(len(self.locations)):
            status = self.locations[self.current_pos]
            print(f"Location {self.current_pos} is {'DIRTY' if status else 'CLEAN'}.")
            
            # If dirty, clean it
            if status == 1:
                print(f"Action: Cleaning {self.current_pos}...")
                self.locations[self.current_pos] = 0
            else:
                print(f"Action: No action needed.")

            # Move to next location
            self.current_pos = 'B' if self.current_pos == 'A' else 'A'
            print(f"Action: Moving to {self.current_pos}...\n")

        print("Environment is now clean.")

# Execution
agent = VacuumAgent()
agent.sense_and_act()
