from dfs import dfs as dfs_search
from bfs import bfs as bfs_search
from dijkstra import dijkstra
from constants import stations_ny, connections_ny, weighted_edges
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph():
    G_ny = nx.Graph()

    G_ny.add_nodes_from(stations_ny)
    G_ny.add_edges_from(connections_ny)

    plt.figure(figsize=(12, 10))
    nx.draw(
        G_ny,
        with_labels=True,
        node_color="lightblue",
        node_size=800,
        edge_color="gray",
        font_size=10,
    )
    plt.title("Модель мережі метро Нью-Йорка")
    plt.show()

    number_of_nodes_ny = G_ny.number_of_nodes()
    number_of_edges_ny = G_ny.number_of_edges()
    degrees_ny = G_ny.degree()

    print(f"Кількість вершин: {number_of_nodes_ny} \n")
    print(f"Кількість ребер: {number_of_edges_ny} \n")
    print(f"Ступені вершин: {dict(degrees_ny)} \n")

    return G_ny


def print_path(path):
    return " → ".join(path)


def add_weighted_edges(graph, edges):
    for edge in edges:
        graph.add_edge(edge[0], edge[1], weight=edge[2])


def main():
    G_ny = draw_graph()

    graph_dict = nx.to_dict_of_lists(G_ny)

    dfs_path = dfs_search(graph_dict, "Times Square", "Atlantic Avenue")
    bfs_path = bfs_search(graph_dict, "Times Square", "Atlantic Avenue")

    print(f"Шлях з використанням DFS: {print_path(dfs_path)} \n")
    print(f"Шлях з використанням BFS: {print_path(bfs_path)} \n")

    G_ny_weighted = nx.Graph()

    add_weighted_edges(G_ny_weighted, weighted_edges)

    start, goal = "Times Square", "Atlantic Avenue"
    shortest_path = dijkstra(G_ny_weighted, start, goal)

    print(
        f"Найкоротший шлях з використанням алгоритму Дейкстри: {print_path(shortest_path)}"
    )


if __name__ == "__main__":
    main()
