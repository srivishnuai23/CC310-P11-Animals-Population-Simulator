# CC310-P11-Animals-Population-Simulator
This project simulates how populations of different organisms change over time in a shared ecosystem. The goal is to model how species interact, compete, and are affected by outside intervention over a long period (10 years, or 3650 days).

Note: This is a console application. All the code is in the Project.py file, and the relevant test txt files are in the tests folder. 

The simulation is driven by four input files, each describing a different aspect of the ecosystem:
- **Relationships between organisms** – defines how population “flows” from one species to another (for example, how much of one species contributes to another’s growth).
- **Hierarchy of organisms** – represents a parent-child structure that helps regulate population balance.
- **Scheduled interventions** – determines when external actions (like conservation efforts) occur.
- **Initial and target populations** – provides starting values and desired population levels for each organism.

**How the Simulation Works**

Each day of the simulation is processed in three steps:
1. **Population Redistribution** 
	- Every organism distributes its population to others based on predefined relationships. A new population is calculated entirely from these incoming contributions.
2. **Population Balancing** 
	- The system checks the hierarchy of organisms. If a species becomes too large or too small compared to its parent, adjustments are made to keep the ecosystem balanced.
3. **External Intervention** 
	- On certain days, conservation efforts are applied. If a population is far from its target, it is either reduced or increased to help stabilize the system.

Purpose of the Project
- This project demonstrates how multiple simple rules can interact to produce complex behavior over time. By combining natural population flow, structural constraints, and periodic intervention, the simulation explores whether ecosystems stabilize, fluctuate, or drift over time.


**Key Features**
- Simulates long-term population changes across multiple species
- Handles dynamic interactions between organisms
- Incorporates both natural processes and human intervention
- Produces precise final population values after 3650 iterations


**Outcome**
- At the end of the simulation, the program outputs the final population of each organism. These results reflect the combined effects of all interactions and adjustments over time.
