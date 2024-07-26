# Vacuum_Cleaner_Implementation
This is the Code for Model based, Utility based and Goal based vacuum agent

# Model-Based Agents

A Model-Based agent is an agent that uses a model of the world.

Current percept is combined with old internal state to generate the updated description of the current state based on the agent’s model of ‘how the world works’. The agent maintains some sort of internal state that depends on the percept history reflecting at least some of the unobserved aspects of the current state.

Updating the internal State information requires two kinds of knowledge to be encoded in the agent program:
1. Information about how the world evolves independently of the agent
2. Information about how the agents actions affect the world

![image](https://github.com/user-attachments/assets/7bc914a8-bb11-48a2-a568-890129716537)

Before you take an action, you have to check what action was previously taken and update the internal state with the action taken. The action taken will decide what the next state will be like.

# BRIEF DESCRIPTION OF THE CODE FOR MODEL BASED AGENT

This repository contains a simple model of a vacuum cleaner agent designed to operate in a environment with two locations: 'A' and 'B'. The vacuum cleaner starts at location 'A', where its initial cleanliness status is determined randomly. 
The environment's state is represented by the cleanliness of both locations. The agent follows a set of predefined rules: if at 'A' and clean, it moves to 'B'; if at 'A' and dirty, it cleans; if at 'B' and clean, it moves to 'A'; and if at 'B' and dirty, it cleans. 
The agent updates its internal state and the environment's state based on these actions. The model runs for a specified number of steps (10 by default), printing the current state, the action taken, and the resulting state after each action. 
This simple model demonstrates the basic principles of an agent-based system in a controlled environment.


# Goal-Based Agents

Understanding the current state of the environment is not always sufficient for deciding what actions to take. Agents require goal information that outlines desirable situations, enabling them to choose actions that achieve these goals. Achieving a goal might require a single action or a sequence of actions

Goal-based decision making considers:
1. The future – what will happen if I do this action?
2. Will that make me happy/ reach goal?

![image](https://github.com/user-attachments/assets/dfee2303-455e-45ab-8313-89af0628fe5c)


# Utility-Based Agents

Goals just provide a crude binary distinction between 'happy' and 'unhappy' states.
Performance measure needs to allow comparison of different world states according to exactly how happy they would make the agent: **Utility Value Maximization**

![image](https://github.com/user-attachments/assets/f56cac13-d998-44b5-8cad-b5efb73a2bd7)









