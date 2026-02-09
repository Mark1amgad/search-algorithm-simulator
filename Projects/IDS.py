# ===============================
# IDS - Traversal Path (not shortest path)
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
# DFS محدد بالعمق مع تسجيل traversal path
# ===============================
def dfs_limited_traversal(graph, node, goal, depth, visited, traversal):
    visited.add(node)
    traversal.append(node)  # تسجيل كل عقدة مشي عليها

    # لو وصلنا للهدف نوقف البحث
    if node == goal:
        return True

    if depth == 0 or node not in graph:
        return False

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs_limited_traversal(graph, neighbor, goal, depth-1, visited, traversal):
                return True

    return False

# ===============================
# IDS مع Traversal Path
# ===============================
def ids_traversal(graph, start, goal, max_depth=100):
    traversal_path = []  # لتسجيل كل ما يمشي عليه البحث

    for depth in range(max_depth + 1):
        visited = set()
        temp_traversal = []
        print(f"Searching at depth: {depth}")
        found = dfs_limited_traversal(graph, start, goal, depth, visited, temp_traversal)

        traversal_path.extend(temp_traversal)  # تسجيل كل ما مشى عليه

        if found:
            print("✅ Goal found!")
            print("Traversal path:")
            print(" -> ".join(map(str, traversal_path)))
            return traversal_path

    print("❌ Goal not found!")
    print("Traversal path:")
    print(" -> ".join(map(str, traversal_path)))
    return traversal_path

# ===============================
# تشغيل البرنامج
# ===============================
goal = int(input("Enter goal node: "))
ids_traversal(graph, 0, goal)
