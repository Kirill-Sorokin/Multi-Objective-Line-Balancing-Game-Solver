# Multi-Objective-Line-Balancing-Game-Solver

This repository contains a Python implementation designed to tackle the Multi-Objective Line Balancing Game, a complex problem that seeks an optimal balance between economic efficiency, social fairness, and environmental sustainability in a manufacturing line setup. The solution integrates several heuristic rules and optimization techniques to assign tasks to workstations while considering constraints like processing times, tool requirements, and the TAKT time.

**Key Features:**

Economic Efficiency: Maximizes the use of resources by optimizing the number of workstations needed versus the total processing time, aiming for line efficiency.
Social Fairness: Ensures a fair distribution of workload among workstations, minimizing variance to promote workplace equity.
Environmental Sustainability: Reduces the environmental impact by minimizing the variety and total number of tools required, reflecting a commitment to sustainable manufacturing practices.

**Technical Highlights:**

Utilization of Python's standard libraries and custom algorithms to generate solutions that balance between economic, social, and environmental objectives.
Implementation of normalization techniques to ensure objective scores are comparable on a scale of 0 to 1, facilitating a weighted-sum approach to evaluate overall solution effectiveness.
Exploration of heuristic rules such as Largest Candidate Rule (LCR), Kilbridge and Wester Rule, and Ranked Positional Weights (RPW) to guide task assignments.

**Potential Applications:**

This solver can be a valuable tool for researchers, students, and professionals in industrial engineering, operations research, and related fields looking for a practical approach to address line balancing problems in manufacturing and production settings. It offers insights into multi-objective optimization and serves as a foundation for further exploration and development of more sophisticated solutions.

**Contribution & Collaboration:**

Contributions to enhance the solver's efficiency, extend its capabilities, or adapt it to specific industrial scenarios are welcome. Whether it's through suggesting new features, optimizing existing algorithms, or providing feedback on usability, your input can help evolve this project into a more comprehensive solution for the line balancing community.
