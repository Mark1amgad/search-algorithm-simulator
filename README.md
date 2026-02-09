# Search Algorithm Simulator – Artificial Intelligence Course

## Overview

This project is a **Search Algorithm Simulator** built for an Artificial Intelligence course to visualize and compare classic graph search algorithms on a shared state space. It is implemented as a Streamlit web application that lets users select an algorithm, configure parameters, and observe how the search explores nodes step by step.

## Features

- Interactive Streamlit web interface for running and visualizing search algorithms.
- Multiple search strategies running on the same graph for direct side‑by‑side comparison.
- Configurable goal node and maximum depth for depth‑limited methods.
- Clear indication of whether the goal was found and the resulting traversal path.
- Basic metrics such as number of visited nodes and solution depth (for IDS).
- Tree-style text visualization of the explored nodes along the path.

## Implemented algorithms

**Uninformed (blind) search**

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Depth-Limited Search (DLS)
- Iterative Deepening Search (IDS)
- Uniform Cost Search (UCS)

**Informed search**

- Greedy Best-First Search

All algorithms operate on the same predefined graph so you can compare traversal order, path length, and search depth under different strategies.

## Tech stack

- Python 3
- Streamlit
- Standard libraries:  
  - `collections.deque` for queue-based BFS
  - `queue.PriorityQueue` for UCS and Greedy Best-First Search

## Project structure

```text
Projects/
  app.py      # Streamlit main app (UI + visualization)
  BFS.py      # Breadth-First Search implementation
  DFS.py      # Depth-First Search implementation
  DLS.py      # Depth-Limited Search implementation
  IDS.py      # Iterative Deepening Search implementation
  UCS.py      # Uniform Cost Search implementation
  GREEDY.py   # Greedy Best-First Search implementation
```

Note: There is also an `app.py` in the repository root, used as an entry point in some environments.

## How to run

1. Clone the repository:

   ```bash
   git clone https://github.com/Mark1amgad/search-algorithm-simulator.git
   cd search-algorithm-simulator/Projects
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # Linux/Mac
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install streamlit
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL shown in the terminal (usually `http://localhost:8501`) in your browser.

## Usage

- Choose an algorithm from the sidebar (BFS, DFS, DLS, IDS, UCS, Greedy Best-First).
- Set the **Goal Node** (an integer within the graph range, for example 0–100).
- For DLS, set the **Maximum Depth** parameter.
- Click **Run Algorithm** to execute the search and view:  
  - Whether the goal was found.
  - The traversal path (order of visited nodes).
  - Basic metrics (nodes visited, depth for IDS) and the tree-style visualization.

## Educational objectives

- Practice implementing classical AI search algorithms in Python.
- Understand the differences between uninformed and informed search strategies.
- Observe how search strategy affects exploration order, performance, and solution depth.
- Provide an interactive tool for students to experiment with and compare search algorithms.

## Contributors

This project was developed as a team assignment for the **AIE111 Artificial Intelligence** course.

- Khaled Amr  
- Hossam Ahmed  
- Abdulrahman Edris  
- Abdalhalem Waleed  
- Ibrahim Abdrabo  
- Mark Amgad
