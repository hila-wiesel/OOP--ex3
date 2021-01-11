import json
import time
import unittest

import matplotlib.pyplot as plt

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import networkx as nx

g1 = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_10_80_1.json"
g2 = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_100_800_1.json"
g3 = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_1000_8000_1.json"
g4 = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_10000_80000_1.json"
g5 = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_20000_160000_1.json"
g6 = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_30000_240000_1.json"
graphs = [g1, g2, g3, g4, g5, g6]


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


def my_shortest_path(file_path: str, src: int, dest: int) -> float:
    algo = GraphAlgo(None)
    algo.load_from_json(file_path)
    # algo.plot_graph()
    start_time = time.perf_counter()
    path = algo.shortest_path(src, dest)
    end_time = time.perf_counter()
    time_myCode = end_time - start_time
    # print_path(path)
    return time_myCode


def nx_shortest_path(file_path: str, src: int, dest: int) -> float:
    g = load_from_json_by_networkx(TestPart3, file_path)
    start_time_nx = time.perf_counter()
    nx.shortest_path(g, source=src, target=dest, weight='weight')
    end_time_nx = time.perf_counter()
    time_nx = end_time_nx - start_time_nx
    # print("time_nx in shortest path:", time_nx, "\n")
    return time_nx


def my_SCCs(file_path: str) -> float:
    algo = GraphAlgo()
    algo.load_from_json(file_path)
    start_time = time.perf_counter()
    sccs = algo.connected_components()
    end_time = time.perf_counter()
    # print("all scc in g:", sccs, "\n")
    time_myCode = end_time - start_time
    return time_myCode


def nx_SCCs(file_path: str) -> float:
    g = load_from_json_by_networkx(TestPart3, file_path)
    start_time_nx = time.perf_counter()
    sccs_nx = list(nx.strongly_connected_components(g))
    end_time_nx = time.perf_counter()
    time_nx = end_time_nx - start_time_nx
    # print("all scc in g:", sccs_nx, "\n")
    return time_nx


def my_scc(file_path: str, id1: int, ) -> float:
    algo = GraphAlgo(None)
    algo.load_from_json(file_path)
    start_time = time.perf_counter()
    sccs = algo.connected_component(id1)
    end_time = time.perf_counter()
    # print("scc in g for specific node:", scc, "\n")
    return end_time-start_time


class TestPart3(unittest.TestCase):

    def test_shortest_path(self):
        my_results = []
        nx_results = []
        for i in range(6):
            my_sum = 0.0
            nx_sum = 0.0
            for j in range(10):
                my_sum += my_shortest_path(graphs[i], i, 10)
               # nx_sum += nx_shortest_path(graphs[i], i, 10)
            my_sum = my_sum/10
            nx_sum = nx_sum/10
            my_results.append(my_sum)
            nx_results.append(nx_sum)

        print("my shortest path: ", my_results)
        # print("nx shortest path: ", nx_results)

    def test_SCCs(self):
        my_results = []
        nx_results = []
        for i in range(6):
            my_sum = 0.0
            nx_sum = 0.0
            for j in range(10):
                add = my_SCCs(graphs[i])
                my_sum += add
                nx_sum += nx_SCCs(graphs[i])
                #print("my_sum =", add)
            my_sum = my_sum/10
            #print("-----> my_sum = ", my_sum, "\n")
            nx_sum = nx_sum/10
            my_results.append(my_sum)
            nx_results.append(nx_sum)

        print("my SCCs: ", my_results)
        print("nx SCCs: ", nx_results)

    def test_mySCC(self):
        my_results = []
        for i in range(6):
            my_sum = 0.0
            for j in range(10):
                my_sum += my_scc(graphs[i], i)
            my_sum = my_sum/10
            my_results.append(my_sum)
        print("my one SCC: ", my_results)

    def test__G_10_80_1(self):
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_10_80_1.json"
        print("Graph 1:")
        print("my time for SCCs:", my_SCCs(file_path))
        print("my time for one SCC:", my_scc(file_path, 1))
        print("my time for shortest_path:", my_shortest_path(file_path, 0, 5))

    def test__G_100_800_1(self):
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_100_800_1.json"
        print("Graph 2:")
        print("my time for SCCs:", my_SCCs(file_path))
        print("my time for one SCC:", my_scc(file_path, 1))
        print("my time for shortest_path:", my_shortest_path(file_path, 0, 5))

    def test__G_1000_8000_1(self):
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_1000_8000_1.json"
        print("Graph 3:")
        print("my time for SCCs:", my_SCCs(file_path))
        print("my time for one SCC:", my_scc(file_path, 1))
        print("my time for shortest_path:", my_shortest_path(file_path, 0, 5))

    def test__G_10000_80000_1(self):
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_10000_80000_1.json"
        print("Graph 4:")
        print("my time for SCCs:", my_SCCs(file_path))
        print("my time for one SCC:", my_scc(file_path, 1))
        print("my time for shortest_path:", my_shortest_path(file_path, 0, 5))

    def test__G_20000_160000_1(self):
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_20000_160000_1.json"
        print("Graph 5:")
        print("my time for SCCs:", my_SCCs(file_path))
        print("my time for one SCC:", my_scc(file_path, 1))
        print("my time for shortest_path:", my_shortest_path(file_path, 0, 5))

    def test__G_30000_240000_1(self):
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_on_circle/G_30000_240000_1.json"
        print("Graph 6:")
        print("my time for SCCs:", my_SCCs(file_path))
        print("my time for one SCC:", my_scc(file_path, 1))
        print("my time for shortest_path:", my_shortest_path(file_path, 0, 5))

