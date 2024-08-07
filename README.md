# Vacuum_Cleaner_Implementation
This is the Code for Model-based, Utility-based, and Goal-based vacuum agents.

# Model-Based Agents

A Model-Based agent is an agent that uses a model of the world.

The current percept is combined with the old internal state to generate the updated description of the current state based on the agent’s model of ‘how the world works.’ The agent maintains an internal state that depends on the percept history reflecting at least some of the unobserved aspects of the current state.

Updating the internal State information requires two kinds of knowledge to be encoded in the agent program:
1. Information about how the world evolves independently of the agent
2. Information about how the agents' actions affect the world

![image](https://github.com/user-attachments/assets/7bc914a8-bb11-48a2-a568-890129716537)

Before you take action, you'll need to check what was previously taken and update the internal state with the action taken. The action taken will decide what the next state will be like.

# BRIEF DESCRIPTION OF THE CODE FOR MODEL-BASED AGENT

This repository contains a simple model of a vacuum cleaner agent designed to operate in an environment with two locations: 'A' and 'B.' The vacuum cleaner starts at location 'A,' where its initial cleanliness status is determined randomly. 
The cleanliness of both locations represents the environment's state. The agent follows a set of predefined rules: if at 'A' and clean, it moves to 'B'; if at 'A' and dirty, it cleans; if at 'B' and clean, it moves to 'A'; and if at 'B' and dirty, it cleans. 
Based on these actions, the agent updates its internal state and the environment's state. The model runs for a specified number of steps (10 by default), printing the current state, the action taken, and the resulting state after each action. 
This simple model demonstrates the basic principles of an agent-based system in a controlled environment.


# Goal-Based Agents

Understanding the current state of the environment is not always sufficient for deciding what actions to take. Agents require goal information that outlines desirable situations, enabling them to choose actions that achieve these goals. Achieving a goal might require a single action or a sequence of actions.

Goal-based decision-making considers the following:
1. The future – what will happen if I do this action?
2. Will that make me happy/ reach my goal?

![image](https://github.com/user-attachments/assets/dfee2303-455e-45ab-8313-89af0628fe5c)

# BRIEF DESCRIPTION OF THE CODE FOR GOAL-BASED AGENT

This code defines a goal-based vacuum cleaner agent whose primary goal is to ensure that both locations 'A' and 'B' are clean. The agent starts at location 'A' with a randomly assigned status of 'Clean' or 'Dirty' for both locations. It determines its actions based on its current location and the cleanliness status of both locations. The agent can move left or right between the two locations or clean the current location if it is dirty. The update_state method updates the internal state based on the action taken, while the rule_match method decides the action required to achieve the goal. The is_goal_achieved method checks if both locations are clean. The run method allows the agent to operate continuously, taking actions and updating its state until the goal of cleaning both locations is achieved. Once both locations are clean, the number of steps taken to achieve the goal is printed.


# Utility-Based Agents

Goals provide a crude binary distinction between 'happy' and 'unhappy' states.
Performance measure needs to allow comparison of different world states according to exactly how happy they would make the agent: **Utility Value Maximization**

![image](https://github.com/user-attachments/assets/f56cac13-d998-44b5-8cad-b5efb73a2bd7)

# BRIEF DESCRIPTION OF THE CODE FOR UTILITY-BASED AGENT

This code defines a UtilityBasedVacuumCleaner class, which models a vacuum cleaner agent operating in a simple environment with two locations, 'A' and 'B.' The agent aims to keep both locations clean, and predefined rules determine its actions. The agent can either move left or right or clean a location.

The agent's performance is measured by a performance metric that decreases when the vacuum cleaner moves unnecessarily (i.e., moves to a location that is already clean). The agent runs for several steps, updating its state and calculating its performance at each step. At the end of the run, the agent's rationality is evaluated based on whether it has traveled unnecessarily five or more times. If the performance measure shows five or more unnecessary moves, the agent is deemed irrational.

# LEARNING OUTCOMES

Model-Based Agents: Learn to create agents using a world model to update internal states and actions.

Goal-Based Agents: Implement agents that make decisions to achieve specific goals.

Utility-Based Agents: Develop agents that optimize performance based on utility values.

Performance and Rationality: Measure agent performance and evaluate rationality based on actions and outcomes.
