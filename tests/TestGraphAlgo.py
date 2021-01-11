import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


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
    print("distance is: ", dist)


class TestGraphAlgo(unittest.TestCase):

    def test_shortestPath(self):
        g = graph_builder(100)
        for i in range(0, 100, 2):
            g.add_edge(i, i + 2, i + 1)
        algo = GraphAlgo(g)
        self.assertIsNotNone(algo.shortest_path(0, 2)[1])
        self.assertEqual(-1, algo.shortest_path(0, 1)[0])
        self.assertIsNone(algo.shortest_path(0, 1)[1])
        src = 2
        dest = 4
        # print_path(algo.shortest_path(src, dest))

    def test_scc_None(self):
        algo = GraphAlgo(None)
        self.assertEqual(0, len(algo.connected_components()))

    def test_scc1(self):
        g = graph_builder(100)
        for i in range(0, 6, 2):
            g.add_edge(i, i + 2, i + 1)
        algo = GraphAlgo(g)
        for j in range(2, 7, 2):
            g.add_edge(j, j - 2, j + 1)
        scc1 = algo.connected_component(0)
        self.assertEqual(len(scc1), 4)
        scc_l1 = algo.connected_components()
        self.assertEqual(len(scc_l1), 97)
        # print("scc of node 0:", scc1)
        # print("list of scc:", algo.connected_components())

    def test_scc2(self):
        g = graph_builder(100)
        algo = GraphAlgo(g)
        for n in g.get_all_v().keys():
            self.assertEqual(1, len(algo.connected_component(n)))
        self.assertEqual(0, len(algo.connected_component(200)))  # un-existed node
        self.assertEqual(100, len(algo.connected_components()))
        # print(algo.connected_components())

    def test_scc3(self):
        g = graph_builder(20)
        algo = GraphAlgo(g)
        for i in range(20):
            g.add_edge(0, i, i)
        self.assertEqual(1, len(algo.connected_component(0)))
        for i in range(2, 20, 2):
            g.add_edge(i, i - 2, i)
        # print("scc of node 0:", algo.connected_component(0))
        # print(algo.connected_component(0))
        self.assertEqual(10, len(algo.connected_component(0)))

    def test_save_load(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_edge(1, 2, 3)
        algo = GraphAlgo(g)
        algo.save_to_json("test1")
        algo.load_from_json("test1")
        self.assertEqual(g.v_size, algo.graph.v_size)
        self.assertEqual(g.e_size, algo.graph.e_size)
        self.assertEqual(g, algo.graph)

    def test_save_load2(self):
        g = DiGraph()
        algo = GraphAlgo(g)
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/data/A5"
        self.assertTrue(algo.load_from_json(file_path))
        algo.plot_graph()

    def test_save_load3(self):
        g = DiGraph()
        algo = GraphAlgo(g)
        file_path = "C:/Users/97252/PycharmProjects/pythonProject1/Graphs_random_pos/G_100_800_2.json"
        self.assertTrue(algo.load_from_json(file_path))
        algo.plot_graph()

    def test_helper_scc(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_edge(0, 1, 3)
        g.add_edge(1, 0, 3)
        algo = GraphAlgo(g)
        algo.bfs(0, 0)
        # print("scc:", algo.connected_component(0))
        # print("done")

    def test_plot(self):
        g = DiGraph()
        g.add_node(0)
        g.get_node(0).set_pos([1, 2])
        g.add_node(1)
        g.get_node(1).set_pos([3, 7])
        g.add_node(3)
        g.get_node(3).set_pos([6, 2])
        g.add_node(4)
        g.get_node(4).set_pos([9, 1])
        g.add_edge(0, 1, 3)
        g.add_edge(0, 3, 3)
        g.add_edge(3, 1, 3)
        algo = GraphAlgo(g)
        algo.save_to_json("test1")
        algo.load_from_json("test1")
        algo.plot_graph()

    def test_plot2(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        for i in range(6):
            g.add_edge(i, i+1, 3)
        g.add_edge(6, 0, 3)
        algo = GraphAlgo(g)
        algo.plot_graph()
