from collections import defaultdict
from math import sqrt
import random

# Constants and Task Definitions
TAKT_TIME = 56
MAX_STD_DEV = 13
VARIETY_OF_TOOLS = 3
WEIGHTS = {'economic': 5, 'social': 9, 'environmental': 7}

# Task definitions
graph = defaultdict(list,{
    1: [3], 3: [6], 6: [10, 11], 10: [14], 14: [18], 18: [22, 23], 22: [26],
    11: [14, 15], 23: [26, 27], 26: [27, 29], 2: [4, 9], 4: [7, 8], 7: [11, 12],
    15: [18, 19, 16], 19: [23, 20], 29: [30], 12: [15, 13], 24: [27, 28], 27: [29],
    5: [8], 8: [13], 16: [20], 20: [24, 25], 13: [16, 17], 25: [28], 28: [29], 9: [17],
    17: [21], 21: [25], 30: []
})

processing_times = {
    1: 13, 2: 6, 3: 7, 4: 6, 5: 11, 6: 11, 7: 6, 8: 11, 9: 14, 10: 8, 11: 11, 12: 15,
    13: 14, 14: 5, 15: 12, 16: 6, 17: 7, 18: 15, 19: 6, 20: 10, 21: 11, 22: 7, 23: 10,
    24: 9, 25: 7, 26: 15, 27: 12, 28: 12, 29: 7, 30: 5
}

task_tools = {
    2: 'M1', 3: 'M1', 4: 'M2', 5: 'M1', 8: 'M1', 9: 'M3', 10: 'M3', 11: 'M1', 14: 'M3',
    15: 'M2', 17: 'M2', 18: 'M1', 19: 'M1', 20: 'M1', 21: 'M1', 22: 'M1', 23: 'M3',
    25: 'M3', 27: 'M2', 29: 'M2', 30: 'M3'
}

def standard_deviation(data):
    if len(data) < 2:
        return 0
    mean = sum(data) / len(data)
    return sqrt(sum((x - mean) ** 2 for x in data) / (len(data) - 1))

def calculate_normalized_scores(workstations, processing_times, task_tools):
    total_processing_time = sum(processing_times.values())
    ZEc = total_processing_time / (len(workstations) * TAKT_TIME)
    NEc = ZEc  # Assuming ZEc calculation aligns with NEc normalization

    workstation_loads = [sum(processing_times[task] for task in ws) for ws in workstations]
    ZSo = standard_deviation(workstation_loads)
    NSo = (MAX_STD_DEV - min(ZSo, MAX_STD_DEV)) / MAX_STD_DEV

    tasks_with_tools = sum(1 for task in processing_times if task in task_tools)
    ZEn = len({task_tools[task] for ws in workstations for task in ws if task in task_tools})
    NEn = (tasks_with_tools - ZEn) / (tasks_with_tools - VARIETY_OF_TOOLS) if tasks_with_tools != VARIETY_OF_TOOLS else 1

    weighted_sum = (WEIGHTS['economic'] * NEc + WEIGHTS['social'] * NSo + WEIGHTS['environmental'] * NEn) / sum(WEIGHTS.values())
    
    return NEc, NSo, NEn, weighted_sum

def generate_solution(processing_times):
    tasks = list(processing_times.keys())
    random.shuffle(tasks)  # Shuffle tasks for variety
    workstations = [[]]
    
    for task in tasks:
        current_time = sum(processing_times[t] for t in workstations[-1])
        if current_time + processing_times[task] <= TAKT_TIME:
            workstations[-1].append(task)
        else:
            workstations.append([task])
    
    return workstations

# Main Execution
solutions = [generate_solution(processing_times) for _ in range(1000)]  # More solutions for a diverse set
evaluated_solutions = [(solution, calculate_normalized_scores(solution, processing_times, task_tools)) for solution in solutions]
evaluated_solutions.sort(key=lambda x: x[1][-1], reverse=True)  # Sort by weighted sum

# Display Top 10 Solutions
for i, (solution, scores) in enumerate(evaluated_solutions[:10], start=1):
    print(f"Top {i} Solution:")
    for ws_index, ws in enumerate(solution, start=1):
        print(f"  WS{ws_index}: Tasks {', '.join(map(str, ws))}")
    NEc, NSo, NEn, weighted = scores
    print(f"  Scores - Economic: {NEc:.2f}, Social: {NSo:.2f}, Environmental: {NEn:.2f}, Weighted: {weighted:.2f}\n")
