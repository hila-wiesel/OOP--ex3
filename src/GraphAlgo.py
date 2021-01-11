import json
import random
import sys
from abc import ABC
from typing import List
import queue
import matplotlib.pyplot as plt
import mpmath
from matplotlib.patches import ConnectionPatch

from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface, ABC):

    def __init__(self, graph: DiGraph = None):
        if graph is not None:
            self.graph = graph
        else:
            self.graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        g = DiGraph()
        try:
            with open(file_name, "r") as f:
                details = json.load(f)
                nodes = details.get("Nodes")
                edges_out = details.get("Edges")
                for dic in nodes:
                    key = dic.get("id")
                    pos = dic.get("location")
                    g.add_node(key)
                    g.get_node(key).set_pos(pos)
                for dic in edges_out:
                    g.add_edge(dic.get("src"), dic.get("dest"), dic.get("w"))
                self.graph = g
            return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as file:
                json.dump(self.graph, default=lambda m: m.as_dict(), indent=4, fp=file)
                return True
        except IOError as e:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        This function return the shortest path from src node to dest node
         using the helper function- Dijkstra to get the the previously node from each node that in the shortest path back from dest to src
        :param id1: The start node of the path
        :param id2: The end node of the path
        :return: tuple (distance, the path)
        """
        if id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
            return -1, None
        parents = self.dijkstra(id1)
        dist = self.graph.get_node(id2).get_tag()
        if dist == sys.float_info.max:  # there is no way to get dest from src
            return -1, None
        if id1 == id2:
            path = [id1]
            return 0, path
        p = id2
        path = []
        while parents.get(p) is not None:  # there is a node before him in the path
            path.append(self.graph.get_node(p))
            p = parents.get(p)
        path.append(self.graph.get_node(p))  # add the last node (id1)
        path.reverse()
        return dist, path

    def connected_component(self, id1: int) -> list:
        if self.graph is None or id1 not in self.graph.get_all_v():
            return []
        nodes = self.graph.get_all_v().values()
        for node in nodes:
            node.arrive = False
        way_to = self.bfs(id1, True)
        way_from = self.bfs(id1, False)
        scc = {}
        # print("way_to:", way_to)
        # print("way_from:", way_from)
        for n in way_to.keys():
            if n in way_from.keys():
                scc[n] = 1
        return list(scc.keys())

    def connected_components(self) -> List[list]:
        g = self.graph
        if g is None:
            return []
        scc = []
        saw = []  # node that we already find their scc
        for node in g.get_all_v().values():
            if node not in saw:
                temp_scc = self.connected_component(node.get_key())
                scc.append(temp_scc)
                for n in temp_scc:  # switch to saw.extend(temp_scc)    ??
                    saw.append(n)
        return scc

    def plot_graph(self) -> None:
        g = self.graph
        nodes = g.get_all_v().values()
        max_y = 0
        ax = plt.axes()
        ax.set_title('Graph',  fontsize=14, fontweight='bold')
        ax.set_xlabel('x label')
        ax.set_ylabel('y label')
        for node in nodes:
            if node.get_pos() is None:
                x = 0
                y = 0
                count = 1
                ni_have_pos = False
                if len(node.get_edge_out()) != 0:
                    for ni in node.get_edge_out().keys():
                        n = g.get_node(ni)
                        if n.get_pos() is not None:
                            x += n.get_pos()[0]
                            y += n.get_pos()[1]
                            ++count
                            ni_have_pos = True
                    if ni_have_pos:
                        if count > 2:
                            x = x / count
                            y = y / count
                        else:
                            ni_have_pos = False
                elif len(node.get_edge_in()) != 0:
                    for ni in node.get_edge_in().keys():
                        n = g.get_node(ni)
                        if n.get_pos() is not None:
                            x += n.get_pos()[0]
                            y += n.get_pos()[1]
                            ++count
                            ni_have_pos = True
                    if ni_have_pos:
                        if count > 2:
                            x = x / count
                            y = y / count
                        else:
                            ni_have_pos = False
                if ni_have_pos is False:
                    x = random.randint(0, 100)
                    y = random.randint(0, 100)
                node.set_pos([x, y])
        for node in nodes:
            x = node.get_pos()[0]
            y = node.get_pos()[1]
            if y > max_y:
                max_y = y
            plt.plot(x, y, 'bo')
            ax.annotate(str(node.get_key()), xy=(x, y), xytext=(x - max_y/100, y + max_y/100), color='green',
                        fontsize=12)
            plt.plot(x, y, color='blue', markersize=7, linewidth=7,
                     markerfacecolor='red', markeredgecolor='pink', markeredgewidth=1)
            for e in node.get_edge_out().keys():
                ni = g.get_node(e)
                x_ni = ni.get_pos()[0]
                y_ni = ni.get_pos()[1]
                # ax.arrow(x, y, x_ni-x, y_ni-y, head_width=0.1, head_length=0.3, fc='k', ec='k')
                # plt.arrow(x, y, x_ni-x, y_ni-y, width=0.1, visible=True, in_layout=True, head_width=0.5)
                plt.plot(x_ni, y_ni, color='blue', markersize=7, linewidth=7,
                         markerfacecolor='black', markeredgecolor='pink', markeredgewidth=1)
                connect = ConnectionPatch((x, y), (x_ni, y_ni), "data", "data", arrowstyle="-|>", linewidth=1.5,
                                          mutation_scale=20, fc="pink")
                ax.add_artist(connect)
        plt.show()

    # helper methods:

    def dijkstra(self, src_id: int) -> dict:
        """
        this function use in this class for help an other algorithms get the shortest path between two nodes, the shortest path length and decide whether the graph is connect or not
        by moving from the src node to its neighbors and set their tag (that save distance from src) in accordance to the weight between them,
        and then moving to each of their neighbors and set their tag accordance to the weight between them plus their "parents" tag cetera.
        at the same time Dijkstra saves the parent (previously node) for each node, for using in in other function.
        :param src_id: the id of the start node
        :return: dict of parents
        """
        self.restart()
        g = self.graph
        p_queue = queue.PriorityQueue()
        parents = {src_id: None}
        g.get_node(src_id).set_tag(0.0)  # the distance between node to himself
        p_queue.put(g.get_node(src_id))
        while not p_queue.empty():
            pred = p_queue.get()
            ni = g.all_out_edges_of_node(pred.get_key())
            for key, value in ni.items():  # add to the queue all the neighbors
                temp = g.get_node(key)
                if temp.get_info() == "not visited":
                    p_queue.put(temp)
            for key, value in ni.items():  # updating the right distance (in tag) in the neighbors
                temp = g.get_node(key)
                if temp.get_info() == "not visited":
                    dist = pred.get_tag() + g.get_edge(pred.get_key(), temp.get_key())
                    if dist < temp.get_tag():
                        temp.set_tag(dist)
                        parents[temp.get_key()] = pred.get_key()
            pred.set_info("visited")
        return parents

    def bfs(self, src_id: int, regular: bool) -> dict:
        """
        this function use in this class for help an other algorithms get the Strongly Connected Component of the nodes.
        by moving from the src node to its neighbors and set its arrive field to True, and then moving to each of their
        neighbors and set arrive field to True and et cetera
        in this function there is no restart to arrive field, because we will use this information.
        The restart will be in the algorithms that use it.
        :param src_id:
        :return:    None
        """
        g = self.graph
        src_n = g.get_node(src_id)
        ans = {src_n: 1}
        nodes = g.get_all_v()
        for node in nodes.values():
            node.set_info("white")
        p_queue = queue.PriorityQueue()
        src_n.set_info("gray")
        src_n.arrive = True
        p_queue.put(src_n)
        while not p_queue.empty():
            pred = p_queue.get()
            if regular is True:
                edge = pred.get_edge_out()
            else:
                edge = pred.get_edge_in()
            for ni in edge.keys():
                temp = g.get_node(ni)
                if temp.get_info() != "black":
                    temp.set_info("gray")
                    temp.arrive = True
                    ans[temp] = 1
                    p_queue.put(temp)
            pred.set_info("black")
        return ans

    def restart(self) -> None:
        nodes = self.graph.get_all_v().values()
        my_iter = iter(nodes)
        while True:
            try:
                temp = next(my_iter)
                temp.set_tag(sys.float_info.max)
                temp.set_info("not visited")
            except StopIteration:
                break
