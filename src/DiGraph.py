import sys

from src.GraphInterface import GraphInterface


class DiGraph (GraphInterface):

    class Node:

        def __init__(self, key: int, info: str = "", tag: float = sys.float_info.max, location=None,
                     edge_in: dict = None, edge_out: dict = None):
            self.key = key
            self.info = info
            self.tag = tag
            self.location = location
            if edge_in is None:
                self.edge_in = {}
            else:
                self.edge_in = edge_in
            if edge_out is None:
                self.edge_out = {}
            else:
                self.edge_out = edge_out

        def __str__(self) -> str:
            return str(self.get_key())

        def __repr__(self) -> str:
            return str(self.get_key())

        def __lt__(self, other):
            return self.tag < other.tag

        def as_dict(self) -> dict:
            my_dict = {"id": self.get_key(), "location": self.get_pos()}
            return my_dict

        # getters & setters:

        def get_key(self) -> int:
            return self.key

        def get_info(self) -> str:
            return self.info

        def set_info(self, info: str) -> None:
            self.info = info

        def get_tag(self) -> float:
            return self.tag

        def set_tag(self, tag: float) -> None:
            self.tag = tag

        def get_pos(self) -> list:
            return self.location

        def set_pos(self, location: list) -> None:
            self.location = location

        def get_edge_in(self) -> dict:
            return self.edge_in

        def set_edge_in(self, edge_in: dict) -> None:
            self.edge_in = edge_in

        def get_edge_out(self) -> dict:
            return self.edge_out

        def set_edge_out(self, edge_out: dict) -> None:
            self.edge_out = edge_out

        def has_ni_out(self, id1: int) -> bool:
            if id1 not in self.edge_out:
                return False
            return True

        def has_ni_in(self, id1: int) -> bool:
            if id1 not in self.edge_in:
                return False
            return True

        def add_ni_out(self, id1: int, weight: int) -> None:
            self.edge_out[id1] = weight

        def add_ni_in(self, id1: int, weight: int) -> None:
            self.edge_in[id1] = weight

        def remove_ni_in(self, id1: int) -> None:
            if self.has_ni_in(id1):
                del self.edge_in[id1]

        def remove_ni_out(self, id1: int) -> None:
            if self.has_ni_out(id1):
                del self.edge_out[id1]

    def __init__(self, v_size: int = 0, e_size: int = 0, nodes: dict = None, mc: int = 0):
        self.v_size = v_size
        self.e_size = e_size
        if nodes is None:
            self.nodes = {}
        else:
            self.nodes = nodes
        self.mc = mc

    def __eq__(self, other) -> bool:
        if self.e_size != other.e_size or self.v_size != other.v_size:
            return False
        for n in self.nodes.keys():
            if n not in other.get_all_v().keys():
                return False
            if other.get_all_v().get(n).get_pos() != self.get_node(n).get_pos():
                return False
            # if len(self.all_out_edges_of_node(n)) == 0:
            #     continue
            for edge in self.all_out_edges_of_node(n).items():
                dest = edge[0]
                w = edge[1]
                if not other.has_edge(n, dest):
                    return False
                if other.get_edge(n, dest) != w:
                    return False
        return True

    def as_dict(self) -> dict:
        my_dict = {}
        edges = []
        nodes = []
        for n in self.nodes.values():
            nodes.append(n)
            edge_out = n.get_edge_out()
            for dest in edge_out.keys():
                temp = {"src": n.get_key(), "w": edge_out[dest], "dest": dest}
                edges.append(temp)
        my_dict["Edges"] = edges
        my_dict["Nodes"] = nodes
        return my_dict

    def get_node(self, id1: int) -> Node:
        return self.nodes.get(id1)

    def v_size(self) -> int:
        """Returns the number of vertices in this graph"""
        return self.v_size

    def e_size(self) -> int:
        """Returns the number of edges in this graph"""
        return self.e_size

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        if id1 not in self.get_all_v():
            return None
        return self.get_node(id1).get_edge_in()

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        if id1 not in self.get_all_v():
            return None
        return self.get_node(id1).get_edge_out()

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 == id2 or weight < 0 or id1 not in self.nodes or id2 not in self.nodes:
            return False
        if id2 in self.nodes[id1].get_edge_out():                  # there is an edge between the two
            # if self.nodes[id1].get_edge_out()[id2] == weight:      # with the same weight
            return False
        else:
            n1 = self.nodes[id1]
            n2 = self.nodes[id2]
            n1.add_ni_out(id2, weight)
            n2.add_ni_in(id1, weight)
            self.mc += 1
            self.e_size += 1
            return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        if node_id in self.nodes:
            return False
        new_node = DiGraph.Node(node_id, "", 0.0, pos)
        self.nodes[node_id] = new_node
        self.mc += 1
        self.v_size += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if node_id not in self.nodes:   # node doesnt exist
            return False
        del self.get_all_v()[node_id]   # delete the node
        self.v_size -= 1
        num_del_edges = 0
        for node in self.get_all_v().values():   # delete his edges
            ni_in = node.get_edge_in()
            if node_id in ni_in:
                del ni_in[node_id]
                num_del_edges += 1
            ni_out = node.get_edge_out()
            if ni_out.get(node_id) is not None:
                del ni_out[node_id]
                num_del_edges += 1
        self.e_size -= num_del_edges
        # self.mc -= (num_del_edges+1)
        --self.mc;
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        n1 = self.get_all_v().get(node_id1)
        n2 = self.get_all_v().get(node_id2)
        if n1 is None or n2 is None:     # node doesn't exist
            return False
        if n1.has_ni_out(node_id2) is False:    # edge doesn't exist
            return False
        # delete the edge:
        n1.remove_ni_out(node_id2)
        n2.remove_ni_in(node_id1)
        self.e_size -= 1
        self.mc += 1
        return True

    def has_edge(self, id1: int, id2: int) -> bool:
        """ Return whether there is edge between node id1 to node id2 or not."""
        if id1 not in self.nodes or id2 not in self.nodes:
            return False
        return self.nodes[id1].has_ni_out(id2)

    def get_edge(self, id1: int, id2: int) -> float:
        """ Return the edge between node id1 to node id2. Return -1 if there is no edge between them."""
        if id1 not in self.nodes or id2 not in self.nodes:
            return -1
        edge_out = self.get_node(id1).get_edge_out()
        if id2 not in edge_out:
            return -1
        return edge_out[id2]


