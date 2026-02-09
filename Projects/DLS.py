# ===============================
# DLS - Depth Limited Search
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
# DLS - DFS محدود بالعمق مع traversal path
# ===============================
def dls(graph, node, goal, depth, visited, traversal):
    visited.add(node)
    traversal.append(node)

    # إذا وصلنا الهدف نوقف
    if node == goal:
        return True

    if depth == 0 or node not in graph:
        return False

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dls(graph, neighbor, goal, depth-1, visited, traversal):
                return True

    return False

# ===============================
# تشغيل DLS
# ===============================
def run_dls(graph, start, goal, max_depth):
    visited = set()
    traversal_path = []
    print(f"Running DLS with max depth: {max_depth}")

    found = dls(graph, start, goal, max_depth, visited, traversal_path)

    if found:
        print("✅ Goal found!")
    else:
        print("❌ Goal not found!")

    print("Traversal path:")
    print(" -> ".join(map(str, traversal_path)))
    return traversal_path

# ===============================
# تنفيذ البرنامج
# ===============================
goal = int(input("Enter goal node: "))
max_depth = int(input("Enter maximum depth for DLS: "))
run_dls(graph, 0, goal, max_depth)
