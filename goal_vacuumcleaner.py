import random

class GoalBasedVacuumCleaner:
    def __init__(self):
        # Initialize the agent with a hardcoded initial location 'A'
        self.location = 'A'
        # Randomly choose the initial status as Clean or Dirty
        self.status = random.choice(['Clean', 'Dirty'])
        # Initialize the previous action as None
        self.previous_action = None
        # Initialize the environment state
        self.state = {'A': self.status, 'B': random.choice(['Clean', 'Dirty'])}

        # Define the goal state where both locations are clean
        self.goal_state = {'A': 'Clean', 'B': 'Clean'}

    def update_state(self, action):
        # Update the internal state based on the action taken
        self.previous_action = action  # Update the previous action
        if action == 'Move Right':
            self.location = 'B'
            self.status = self.state[self.location]  # Assuming we know the state of B
        elif action == 'Move Left':
            self.location = 'A'
            self.status = self.state[self.location]  # Assuming we know the state of A
        elif action == 'Clean':
            self.status = 'Clean'
            self.state[self.location] = 'Clean'

    def rule_match(self):
        # Decide the action based on the current state and the goal
        if self.state[self.location] == 'Dirty':
            return 'Clean'
        elif self.location == 'A' and self.state['B'] == 'Dirty':
            return 'Move Right'
        elif self.location == 'B' and self.state['A'] == 'Dirty':
            return 'Move Left'
        else:
            return 'NoOp'  # No operation needed if both are clean

    def is_goal_achieved(self):
        # Check if the current state matches the goal state
        return self.state == self.goal_state

    def run(self, max_steps=10):
        # Run the vacuum cleaner agent until the goal is achieved or max steps are reached
        steps = 0
        while not self.is_goal_achieved() and steps < max_steps:
            print(f"Internal State -\nLocation: {self.location}, Status: {self.status}\nPrevious Action: {self.previous_action}")
            action = self.rule_match()

            print(f"\nAction Taken -\n{action}")

            self.update_state(action)

            print(f"\nNext State -\nLocation: {self.location}, Status: {self.state[self.location]}\n")

            steps += 1

        if self.is_goal_achieved():
            print("Goal achieved: Both locations are clean.")
        else:
            print("Goal not achieved: Reached maximum steps.")

# Calling functions
vacuum_agent = GoalBasedVacuumCleaner()
vacuum_agent.run()


