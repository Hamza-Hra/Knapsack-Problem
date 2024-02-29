# Knapsack Problem Solver with Local Search

## Overview
This Python project aims to solve the classic Knapsack Problem using a variety of approaches. The primary focus is on implementing a simple yet effective local search heuristic to find near-optimal solutions for the knapsack problem instances.

## Features
- **Greedy Algorithm:** An initial solution is obtained using a greedy algorithm that selects items based on their value-to-weight ratio.
- **Local Search Heuristic:** A simple local search algorithm is implemented to iteratively refine the initial solution, exploring the neighborhood for improvements.
- **Dynamic Programming (Optional):** Additionally, an optional dynamic programming approach is included for users to compare against the local search heuristic.

## Implementation
The project is implemented in Python and organized into well-structured modules. The main functionalities are encapsulated in separate files, promoting modularity and ease of maintenance.

## Usage
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/knapsack-problem.git
    ```

2. Navigate to the project directory:
    ```bash
    cd knapsack-problem
    ```

3. Run the main script with your chosen knapsack instance file:
    ```bash
    python main.py your_instance_file.txt
    ```

4. Optionally, explore and modify the implementation or add your own knapsack instances for testing.

## Knapsack Instance File Format
Each knapsack instance file should follow a specific format:
- Line 1: Total number of items (integer)
- Line 2: Knapsack capacity (integer)
- Lines 3 onwards: Each line represents an item with weight and value separated by a space

Example:
