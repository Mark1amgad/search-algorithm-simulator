from queue import PriorityQueue

# ===============================
# تعريف الجراف مع نفس البنية
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
# UCS مع تسجيل Traversal Path
# ===============================
def ucs_traversal(graph, start, goal):
    visited = set()
    traversal_path = []

    # كل عنصر في الـ PriorityQueue = (cost, current_node, path_so_far)
    pq = PriorityQueue()
    pq.put((0, start, [start]))

    while not pq.empty():
        cost, current, path = pq.get()

        if current in visited:
            continue

        visited.add(current)
        traversal_path.append(current)  # تسجيل كل عقدة تم المرور عليها

        # إذا وصلنا الهدف نوقف
        if current == goal:
            print("✅ Goal found!")
            print("Traversal path:")
            print(" -> ".join(map(str, traversal_path)))
            return traversal_path

        # إضافة الأبناء للـ PriorityQueue
        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    pq.put((cost + 1, neighbor, path + [neighbor]))

    print("❌ Goal not found!")
    print("Traversal path:")
    print(" -> ".join(map(str, traversal_path)))
    return traversal_path

# ===============================
# تشغيل البرنامج
# ===============================
goal = int(input("Enter goal node: "))
ucs_traversal(graph, 0, goal)
