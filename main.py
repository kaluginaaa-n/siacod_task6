def tarjan_topological_sort(graph):
    visited = set()
    result = []
    temp_stack = set()

    def dfs(node):
        if node in temp_stack:
            raise ValueError("Граф содержит цикл! Топологическая сортировка невозможна.")

        if node not in visited:
            temp_stack.add(node)
            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)

            temp_stack.remove(node)
            result.append(node)

    for node in graph:
        dfs(node)

    return result


graph = {
    "Проект": ["Lib1", "Lib2", "Lib3"],
    "Lib1": ["Lib4"],
    "Lib2": ["Lib6", "Lib7"],
    "Lib3": [],
    "Lib4": ["Lib5", "Lib6"],
    "Lib5": [],
    "Lib6": [],
    "Lib7": []
}

gr = tarjan_topological_sort(graph)
print("Порядок установки библиотек:")
for lib in gr:
    print(lib)

