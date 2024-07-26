# Vacuum_Cleaner_Implementation
This is the Code for Model based, Utility based and Goal based vacuum agent

# Model-Based Agents

A Model-Based agent is an agent that uses a model of the world.

Current percept is combined with old internal state to generate the updated description of the current state based on the agent’s model of ‘how the world works’. The agent maintains some sort of internal state that depends on the percept history reflecting at least some of the unobserved aspects of the current state.

![image](https://github.com/user-attachments/assets/7bc914a8-bb11-48a2-a568-890129716537)

Before you take an action, you have to check what action was previously taken and update the internal state with the action taken. The action taken will decide what the next state will be like.

# BRIEF DESCRIPTION OF THE CODE FOR MODEL BASED AGENT

This repository contains a simple model of a vacuum cleaner agent designed to operate in a environment with two locations: 'A' and 'B'. The vacuum cleaner starts at location 'A', where its initial cleanliness status is determined randomly. 
The environment's state is represented by the cleanliness of both locations. The agent follows a set of predefined rules: if at 'A' and clean, it moves to 'B'; if at 'A' and dirty, it cleans; if at 'B' and clean, it moves to 'A'; and if at 'B' and dirty, it cleans. 
The agent updates its internal state and the environment's state based on these actions. The model runs for a specified number of steps (10 by default), printing the current state, the action taken, and the resulting state after each action. 
This simple model demonstrates the basic principles of an agent-based system in a controlled environment.


