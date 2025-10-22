import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


class Graph_structure:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        """เพิ่มเส้นเชื่อมระหว่าง node และ neighbor"""
        if node not in self.graph:
            self.graph[node] = []
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        self.graph[node].append(neighbor)
        self.graph[neighbor].append(node)

    def show_graph(self):
        """แสดงโครงสร้าง Graph"""
        for node, neighbors in self.graph.items():
            print(f"{node} -> {neighbors}")

    def plot_graph(self, highlight_nodes=None, title='Graph Visualization'):
        """วาดกราฟด้วย matplotlib และ networkx"""
        G = nx.Graph()
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(10, 8))

        # กำหนดสีของ node
        node_colors = []
        for n in G.nodes():
            if highlight_nodes and n in highlight_nodes:
                node_colors.append('lightcoral')
            else:
                node_colors.append('skyblue')

        nx.draw(
            G, pos,
            with_labels=True,
            node_color=node_colors,
            node_size=1200,
            font_size=12,
            font_weight='bold',
            edge_color='gray'
        )
        plt.title(title)
        plt.show()

    def bfs(self, start):
        if start not in self.graph:
            print(f"Node {start} ไม่อยู่ในกราฟ")
            return []

        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            print(f"เยี่ยมชม node: {node}")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs(self, start):
        if start not in self.graph:
            print(f"Node {start} ไม่อยู่ในกราฟ")
            return []

        visited = set()
        stack = [start]
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                print(f"เยี่ยมชม node: {node}")

                for neighbor in sorted(self.graph[node], reverse=True):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result


if __name__ == "__main__":
    # สร้าง graph
    g = Graph_structure()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('D', 'E')

    print("=" * 50)
    print("โครงสร้าง Graph:")
    print("=" * 50)
    g.show_graph()

    print("\n" + "=" * 50)
    print("BFS เริ่มจาก node 'A':")
    print("=" * 50)
    bfs_result = g.bfs('A')
    print(f"ลำดับการเยี่ยมชม: {' -> '.join(bfs_result)}")

    print("\n" + "=" * 50)
    print("DFS (Iterative) เริ่มจาก node 'A':")
    print("=" * 50)
    dfs_result = g.dfs('A')
    print(f"ลำดับการเยี่ยมชม: {' -> '.join(dfs_result)}")

    # วาดกราฟ
    g.plot_graph(highlight_nodes=bfs_result, title='Graph Structure')