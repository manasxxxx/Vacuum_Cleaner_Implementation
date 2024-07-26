import random

class ModelVacuumCleaner:
    def __init__(self):
        # Initialize the agent with a hardcoded initial location 'A'
        self.location = 'A'
        # Randomly choose the initial status as Clean or Dirty
        self.status = random.choice(['Clean', 'Dirty'])
        # Initialize the previous action as None
        self.previous_action = None
        self.state = {'A': self.status, 'B': random.choice(['Clean', 'Dirty'])} 

        self.model = self.state  # Model tells how the next state depends on current state and action
        self.rules = {
            ('A', 'Clean'): 'Move Right',
            ('A', 'Dirty'): 'Clean',
            ('B', 'Clean'): 'Move Left',
            ('B', 'Dirty'): 'Clean'
        }

    def update_state(self, action):
        # Update the internal state based on the action taken
        self.previous_action = action  # Update the previous action
        if action == 'Move Right':
            self.location = 'B'
            self.status = random.choice(['Clean', 'Dirty'])
        elif action == 'Move Left':
            self.location = 'A'
            self.status = random.choice(['Clean', 'Dirty'])
        elif action == 'Clean':
            self.status = 'Clean'

        self.state[self.location] = self.status
    
    def rule_match(self):
        # Match the rule based on the current state
        return self.rules[(self.location, self.state[self.location])]


    def run(self, steps=10):
        # Run the vacuum cleaner agent for a given number of steps (we put it as 10)
        for _ in range(steps):
            print(f"Internal State -\nLocation: {self.location}, Status: {self.status}\nPrevious Action: {self.previous_action}")
            action = self.rule_match()

            print(f"\nAction Taken -\n{action}")

            self.update_state(action)

            if action == 'Clean':
                # If the action was Clean, print the next state with the updated status
                print(f"\nNext State -\nLocation: {self.location}, Status: {self.status}\n")
            else:
                # If the action was 'Move Right' or 'Move Left', print the next state with the updated location
                print(f"\nNext State -\nLocation: {self.location}\n")

# Calling functions
vacuum_agent = ModelVacuumCleaner()
vacuum_agent.run()
