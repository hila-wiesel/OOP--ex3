import json
import time
import unittest

import matplotlib.pyplot as plt

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import networkx as nx


def graph_builder(size: int) -> DiGraph:
    g = DiGraph()
    for i in range(size):
        g.add_node(i)
    return g


def print_path(shortest: tuple) -> None:
    dist = shortest[0]
    path = shortest[1]
    if path is not None:
        print("Path between ", path[0], "to", path[len(path) - 1], ":")
        for i in range(len(path)):
            print(path[i], sep=",")
    else:
        print("There is no path between the two")
    # print("distance is: ", dist)


def load_from_json_by_networkx(self, file_name: str) -> DiGraph:
    g = nx.DiGraph()
    try:
        with open(file_name, "r") as f:
            details = json.load(f)
            nodes = details.get("Nodes")
            edges_out = details.get("Edges")
            for dic in nodes:
                g.add_node(dic.get("id"))
            for dic in edges_out:
                g.add_weighted_edges_from([(dic.get("src"), dic.get("dest"), dic.get("w"))])
            self.graph = g
        return g
    except Exception as e:
        print(e)
        return None


def shortest_path(file_path: str, src: int, dest: int) -> bool:

    # my code
    algo = GraphAlgo(None)
    algo.load_from_json(file_path)
    # algo.plot_graph()
    start_time = time.perf_counter()
    path = algo.shortest_path(src, dest)
    end_time = time.perf_counter()
    time_myCode = end_time - start_time

    # networkx:
    g2 = load_from_json_by_networkx(TestPart3, file_path)
    # nx.draw(g2, with_labels=True, font_weight='bold')
    # plt.subplot(122)
    # nx.draw_shell(g2, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
    # plt.show()

    start_time_nx = time.perf_counter()
    path_nx = nx.shortest_path(g2, source=src, target=dest, weight='weight')
    end_time_nx = time.perf_counter()
    time_nx = end_time_nx - start_time_nx

    print_path(path)
    print("shortest path in g2", path_nx, "\n")
    print("time_myCode in shortest path:", time_myCode)
    print("time_nx in shortest path:", time_nx, "\n")


def scc_all(file_path: str) -> bool:

    # my code
    algo = GraphAlgo(None)
    algo.load_from_json(file_path)
    start_time = time.perf_counter()
    sccs = algo.connected_components()
    end_time = time.perf_counter()
    print("all scc in g:", sccs, "\n")
    time_myCode = end_time - start_time

    # networkx:
    g2 = load_from_json_by_networkx(TestPart3, file_path)
    start_time_nx = time.perf_counter()
    sccs_nx = list(nx.strongly_connected_components(g2))
    end_time_nx = time.perf_counter()
    time_nx = end_time_nx - start_time_nx

    print("all scc in g:", sccs)
    print("all scc in g2:", sccs_nx, "\n")
    print("time_myCode in sccs:", time_myCode)
    print("time_nx in sccs:", time_nx)


def scc(file_path: str, id1: int, ) -> bool:
    # my code
    algo = GraphAlgo(None)
    algo.load_from_json(file_path)
    start_time = time.perf_counter()
    sccs = algo.connected_component(id1)
    end_time = time.perf_counter()
    print("all scc in g:", sccs, "\n")
    print("time for scc", end_time-start_time)




class TestPart3(unittest.TestCase):

    def test__G_10_80_1(self):
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_10_80_1.json"
        print("Graph 1:")
        shortest_path(file_path, 0, 5)
        scc_all(file_path)
        scc(scc_all, 0)

    def test__G_100_800_1(self):
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_100_800_1.json"
        print("Graph 2:")
        shortest_path(file_path, 0, 5)
        scc_all(file_path)
        scc(scc_all, 0)

    def test__G_1000_8000_1(self):
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_1000_8000_1.json"
        print("Graph 3:")
        shortest_path(file_path, 0, 5)
        scc_all(file_path)
        scc(scc_all, 0)

    def test__G_10000_80000_1(self):
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_10000_80000_1.json"
        print("Graph 4:")
        shortest_path(file_path, 0, 5)
        scc_all(file_path)
        scc(scc_all, 0)

    def test__G_20000_160000_1(self):
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_20000_160000_1.json"
        print("Graph 5:")
        shortest_path(file_path, 0, 5)
        scc_all(file_path)
        scc(scc_all, 0)

    def test__G_30000_240000_1(self):
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_30000_240000_1.json"
        print("Graph 6:")
        # shortest_path(file_path, 0, 5)
        scc_all(file_path)
        # scc(scc_all, 0)

