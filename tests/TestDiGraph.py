import unittest
from src.DiGraph import DiGraph


def graph_builder(size: int) -> DiGraph:
    g = DiGraph()
    for i in range(size):
        g.add_node(i)
    return g


class TestDiGraph(unittest.TestCase):

    def test_addEdge(self):
        g = graph_builder(10)
        for i in range(0, 10, 2):
            print(i)
            g.add_edge(i, i + 2, i)
        for i in range(0, 6, 2):
            print(i)
            self.assertTrue(g.has_edge(i, i+2))
            self.assertFalse(g.has_edge(i+1, i+3))

    def test_addEdge_same(self):
        g = graph_builder(10)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 2, 1)
        g.add_edge(0, 3, 1)
        expect = g.all_out_edges_of_node(0).__sizeof__()
        g.add_edge(0, 0, 2)
        g.add_edge(0, 1, 2)
        self.assertEqual(expect, g.all_out_edges_of_node(0).__sizeof__())

    def test_addEdge_notExist(self):
        g = graph_builder(1)
        self.assertFalse(g.add_edge(0, 1, 12))
        self.assertEqual(1, g.get_mc())

    def test_remove_node(self):
        g = graph_builder(10)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 2, 1)
        g.add_edge(0, 3, 1)
        g.add_edge(5, 0, 1)
        g.add_edge(5, 3, 1)
        g.remove_node(0)
        print("1 =", g.e_size)
        # self.assertEqual(1, g.e_size())     # ##????

    def test_remove_null(self):
        g = graph_builder(0)
        self.assertFalse(g.remove_node(0))

    def test_remove_edge(self):
        g = graph_builder(10)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 2, 1)
        g.add_edge(3, 0, 1)
        g.remove_edge(0, 1)
        g.remove_edge(2, 3)
        e = g.e_size
        print("2 =", g.e_size)
        self.assertEqual(2, e)











