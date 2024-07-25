import random

class VacuumCleanerAgent:
    def __init__(self):
        # Initialize the agent with a hardcoded initial location 'A'
        self.location = 'A'
        # Randomly choose the initial status as 'Clean' or 'Dirty'
        self.status = random.choice(['Clean', 'Dirty'])
        # Initialize the previous action as None
        self.previous_action = None

    def update_status(self):
        # Randomly update the status of the current location to 'Clean' or 'Dirty'
        self.status = random.choice(['Clean', 'Dirty'])

    def decide_action(self):
        # Decide the next action based on the current status and location
        if self.status == 'Dirty':
            # If the status is 'Dirty', the action should be 'Clean'
            action = 'Clean'
        else:
            # If the status is 'Clean', decide the action based on the location
            if self.location == 'A':
                # If the location is 'A' and it is clean, move to the right (to location 'B')
                action = 'Move Right'
            else:
                # If the location is 'B' and it is clean, move to the left (to location 'A')
                action = 'Move Left'
        return action

    def update_state(self, action):
        # Update the internal state based on the action taken
        self.previous_action = action  # Update the previous action
        if action == 'Move Right':
            # If the action is 'Move Right', update the location to 'B'
            self.location = 'B'
            # Randomly update the status of the new location 'B'
            self.update_status()
        elif action == 'Move Left':
            # If the action is 'Move Left', update the location to 'A'
            self.location = 'A'
            # Randomly update the status of the new location 'A'
            self.update_status()
        elif action == 'Clean':
            # If the action is 'Clean', update the status to 'Clean'
            self.status = 'Clean'

    def run(self, steps=10):
        # Run the vacuum cleaner agent for a given number of steps (default is 10)
        for _ in range(steps):
            # Print the current internal state
            print(f"Internal State -\nLocation: {self.location}, Status: {self.status}\nPrevious Action: {self.previous_action}")
            # Decide the next action based on the current state
            action = self.decide_action()
            # Print the action taken
            print(f"\nAction Taken -\n{action}")
            # Update the state based on the action taken
            self.update_state(action)
            # Print the next state after taking the action
            if action == 'Clean':
                # If the action was 'Clean', print the next state with the updated status
                print(f"\nNext State -\nLocation: {self.location}, Status: {self.status}\n")
            else:
                # If the action was 'Move Right' or 'Move Left', print the next state with the updated location
                print(f"\nNext State -\nLocation: {self.location}\n")

# Create an instance of the vacuum cleaner agent and run it
vacuum_agent = VacuumCleanerAgent()
vacuum_agent.run()
