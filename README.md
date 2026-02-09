# Search Algorithm Simulator – Artificial Intelligence Course

## Overview
This project is a **Search Algorithm Simulator** built for an Artificial Intelligence course to visualize and compare classic graph search algorithms on a shared state space. It is implemented as a Streamlit web app that lets users select an algorithm, configure parameters, and see how the search explores nodes step by step.

## Features
- Interactive Streamlit web interface.
- Multiple search strategies on the same graph for easy comparison.
- Configurable goal node and maximum depth (for depth-limited methods).
- Clear indication of whether the goal was found and the traversal path.
- Simple metrics such as nodes visited and depth found (for IDS).
- Tree-style text visualization of the explored nodes along the path.

## Implemented Algorithms
**Uninformed (blind) search:**
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Depth-Limited Search (DLS)
- Iterative Deepening Search (IDS)
- Uniform Cost Search (UCS)

**Informed search:**
- Greedy Best-First Search

All algorithms run on the same predefined graph so you can compare traversal order, path length, and search depth.

## Tech Stack
- Python 3
- Streamlit
- Standard libraries:
  - `collections.deque` for queue-based BFS
  - `queue.PriorityQueue` for UCS and Greedy Best-First Search

## Project Structure
```text
Projects/
  app.py        # Streamlit main app (UI + visualization)
  BFS.py        # Breadth-First Search implementation
  DFS.py        # Depth-First Search implementation
  DLS.py        # Depth-Limited Search implementation
  IDS.py        # Iterative Deepening Search implementation
  UCS.py        # Uniform Cost Search implementation
  GREEDY.py     # Greedy Best-First Search implementation
