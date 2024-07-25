import random

class VacuumCleanerAgent:
    def __init__(self):
        self.location = 'A'  # Hardcoded initial location
        self.status = random.choice(['Clean', 'Dirty'])  # Random initial status
        self.previous_action = None

    def update_status(self):
        """Randomly update the status of the current location."""
        self.status = random.choice(['Clean', 'Dirty'])

    def decide_action(self):
        """Decide the next action based on the current state and the previous action."""
        if self.status == 'Dirty':
            action = 'Clean'
        else:
            if self.location == 'A':
                action = 'Move Right'
            else:
                action = 'Move Left'
        return action

    def update_state(self, action):
        """Update the internal state based on the action taken."""
        self.previous_action = action
        if action == 'Move Right':
            self.location = 'B'
            self.update_status()
        elif action == 'Move Left':
            self.location = 'A'
            self.update_status()
        elif action == 'Clean':
            self.status = 'Clean'

    def run(self, steps=10):
        """Run the vacuum cleaner agent for a given number of steps."""
        for _ in range(steps):
            print(f"Internal State -\nLocation: {self.location}, Status: {self.status}\nPrevious Action: {self.previous_action}")
            action = self.decide_action()
            print(f"\nAction Taken -\n{action}")
            self.update_state(action)
            if action == 'Clean':
                print(f"\nNext State -\nLocation: {self.location}, Status: {self.status}\n")
            else:
                print(f"\nNext State -\nLocation: {self.location}\n")

# Create an instance of the vacuum cleaner agent and run it
vacuum_agent = VacuumCleanerAgent()
vacuum_agent.run()
