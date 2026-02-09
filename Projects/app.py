import streamlit as st
from collections import deque
from queue import PriorityQueue

# ===============================
# تعريف الجراف
# ===============================
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [7, 8],
    4: [9, 10],
    5: [11, 12],
    6: [13, 14],
    7: [15, 16], 
    8: [17, 18],
    9: [19, 20], 
    10: [21, 22],
    11: [23, 24],
    12: [25, 26],
    13: [27, 28], 
    14: [29, 30],
    15: [31, 32],
    16: [33, 34],
    17: [35, 36],
    18: [37, 38],
    19: [39, 40],
    20: [41, 42],
    21: [43, 44],
    22: [45, 46],
    23: [47, 48],
    24: [49, 50],
    25: [51, 52],
    26: [53, 54],
    27: [55, 56],
    28: [57, 58],
    29: [59, 60],
    30: [61, 62],
    31: [63, 64],
    32: [65, 66],
    33: [67, 68],
    34: [69, 70],
    35: [71, 72],
    36: [73, 74],
    37: [75, 76],
    38: [77, 78],
    39: [79, 80],
    40: [81, 82],
    41: [83, 84],
    42: [85, 86],
    43: [87, 88],
    44: [89, 90],
    45: [91, 92],
    46: [93, 94],
    47: [95, 96],
    48: [97, 98],
    49: [99, 100],
}

# ===============================
# BFS Function
# ===============================
def bfs_traversal(graph, start, goal):
    visited = set()
    queue = deque()
    traversal_path = []

    queue.append(start)
    visited.add(start)

    while queue:
        current = queue.popleft()
        traversal_path.append(current)

        if current == goal:
            return True, traversal_path

        if current not in graph:
            continue

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False, traversal_path

# ===============================
# DFS Function
# ===============================
def dfs_traversal(graph, start, goal):
    visited = set()
    traversal_path = []

    def dfs(node):
        if node in visited:
            return False

        visited.add(node)
        traversal_path.append(node)

        if node == goal:
            return True

        if node not in graph:
            return False

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        return False

    found = dfs(start)
    return found, traversal_path

# ===============================
# DLS Function
# ===============================
def dls(graph, node, goal, depth, visited, traversal):
    visited.add(node)
    traversal.append(node)

    if node == goal:
        return True

    if depth == 0 or node not in graph:
        return False

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dls(graph, neighbor, goal, depth-1, visited, traversal):
                return True

    return False

def run_dls(graph, start, goal, max_depth):
    visited = set()
    traversal_path = []
    found = dls(graph, start, goal, max_depth, visited, traversal_path)
    return found, traversal_path

# ===============================
# IDS Function
# ===============================
def dfs_limited_traversal(graph, node, goal, depth, visited, traversal):
    visited.add(node)
    traversal.append(node)

    if node == goal:
        return True

    if depth == 0 or node not in graph:
        return False

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs_limited_traversal(graph, neighbor, goal, depth-1, visited, traversal):
                return True

    return False

def ids_traversal(graph, start, goal, max_depth=100):
    traversal_path = []

    for depth in range(max_depth + 1):
        visited = set()
        temp_traversal = []
        found = dfs_limited_traversal(graph, start, goal, depth, visited, temp_traversal)
        traversal_path.extend(temp_traversal)

        if found:
            return True, traversal_path, depth

    return False, traversal_path, max_depth

# ===============================
# UCS Function
# ===============================
def ucs_traversal(graph, start, goal):
    visited = set()
    traversal_path = []

    pq = PriorityQueue()
    pq.put((0, start, [start]))

    while not pq.empty():
        cost, current, path = pq.get()

        if current in visited:
            continue

        visited.add(current)
        traversal_path.append(current)

        if current == goal:
            return True, traversal_path

        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    pq.put((cost + 1, neighbor, path + [neighbor]))

    return False, traversal_path

# ===============================
# Greedy Function
# ===============================
def greedy_traversal(graph, start, goal):
    visited = set()
    traversal_path = []

    pq = PriorityQueue()
    pq.put((abs(goal - start), start, [start]))

    while not pq.empty():
        h, current, path = pq.get()

        if current in visited:
            continue

        visited.add(current)
        traversal_path.append(current)

        if current == goal:
            return True, traversal_path

        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    pq.put((abs(goal - neighbor), neighbor, path + [neighbor]))

    return False, traversal_path

# ===============================
# Function to build tree representation
# ===============================
def build_tree_text(graph, path):
    tree_lines = []
    visited_in_path = set(path)
    
    def add_node(node, prefix="", is_last=True):
        if node not in visited_in_path:
            return
            
        marker = "└── " if is_last else "├── "
        in_path = "✓" if node in path else ""
        tree_lines.append(f"{prefix}{marker}{node} {in_path}")
        
        if node in graph:
            children = [n for n in graph[node] if n in visited_in_path]
            for i, child in enumerate(children):
                extension = "    " if is_last else "│   "
                add_node(child, prefix + extension, i == len(children) - 1)
    
    tree_lines.append("0 ✓ (Start)")
    if 0 in graph:
        children = [n for n in graph[0] if n in visited_in_path]
        for i, child in enumerate(children):
            add_node(child, "", i == len(children) - 1)
    
    return "\n".join(tree_lines)

# ===============================
# Streamlit UI
# ===============================
st.set_page_config(page_title="Search Algorithms", page_icon="🔍", layout="wide")

st.title("🔍 Search Algorithms Comparison: Password Search Algorithms")
st.markdown("---")

# Sidebar للإعدادات
with st.sidebar:
    st.header("⚙️ Settings")
    
    algorithm = st.selectbox(
        "اختر الخوارزمية / Choose Algorithm",
        ["BFS", "DFS", "DLS", "IDS", "UCS", "Greedy Best-First"]
    )
    
    goal = st.number_input(
        "Goal Node",
        min_value=0,
        max_value=100,
        value=50,
        step=1
    )
    
    if algorithm == "DLS":
        max_depth = st.number_input(
            "Maximum Depth",
            min_value=1,
            max_value=20,
            value=5,
            step=1
        )
    
    run_button = st.button("🚀 Run Algorithm", type="primary", use_container_width=True)

# Main content
col1, col2 = st.columns([2, 1])

st.subheader(f"📊 Algorithm: {algorithm}")
    
if run_button:
    with st.spinner("Running algorithm..."):
        if algorithm == "BFS":
            found, path = bfs_traversal(graph, 0, goal)
            algo_name = "Breadth-First Search"
        elif algorithm == "DFS":
            found, path = dfs_traversal(graph, 0, goal)
            algo_name = "Depth-First Search"
        elif algorithm == "DLS":
            found, path = run_dls(graph, 0, goal, max_depth)
            algo_name = "Depth-Limited Search"
        elif algorithm == "IDS":
            found, path, depth_found = ids_traversal(graph, 0, goal)
            algo_name = "Iterative Deepening Search"
        elif algorithm == "UCS":
            found, path = ucs_traversal(graph, 0, goal)
            algo_name = "Uniform Cost Search"
        elif algorithm == "Greedy Best-First":
            found, path = greedy_traversal(graph, 0, goal)
            algo_name = "Greedy Best-First Search"
    
    # النتيجة
    if found:
        st.success("✅ Goal Found!")
    else:
        st.error("❌ Goal Not Found!")
    
    # عرض المعلومات الإضافية
    info_col1, info_col2, info_col3 = st.columns(3)
    with info_col1:
        st.metric("Algorithm", algo_name)
    with info_col2:
        st.metric("Code Length", "2")
    with info_col3:
        st.metric("Total Passwords", "100")
    
    st.info(f"**Nodes Visited:** {len(path)}")
    
    if algorithm == "IDS":
        st.info(f"**Depth Found At:** {depth_found}")
    
    # عرض المسار
    st.subheader("🛤️ Traversal Path:")
    path_str = " → ".join(map(str, path))
    st.code(path_str, language="text")
    
    # عرض Tree Graph
    st.subheader("🌳 Tree Graph:")
    tree_representation = build_tree_text(graph, path)
    st.code(tree_representation, language="text")

# Footer
st.markdown("---")

# Team Section
st.markdown("### 👥 THIS WEBSITE WAS DEVELOPED BY")
team_col1, team_col2, team_col3 = st.columns(3)

with team_col1:
    st.markdown("### **Khaled Amr**")
    st.markdown("### **Hossam Ahmed**")

with team_col2:
    st.markdown("### **Abdulrahman Edris**")
    st.markdown("### **Abdalhalem Waleed**")

with team_col3:
    st.markdown("### **Ibrahim Abdrabo**")
    st.markdown("### **Mark Amgad**")

st.caption("🔬 Graph Search Algorithms Visualization | Start Node: 0")