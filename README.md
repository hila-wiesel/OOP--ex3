# Directed Weighted Graph
### Object oriented programming - ex3
<p align="center">
  <img src="https://github.com/hila-wiesel/OOP--ex3/blob/main/images/graph2.png" width="350" title="hover text">
  <img src="https://github.com/hila-wiesel/OOP--ex3/blob/main/images/graph1.png" width="350" alt="accessibility text">
</p>


This project models data structures on directed weighted graphs, especially finding the shortest path and deciding and strongly connected components. We will use the data structures dictionary for saving collection of nodes for each graph- saving objects by their key, and also for saving collection of in edge and out edge for each node- saving the key of the neighbor and the weight. This data structures provides us easy way to get the nodes (by their key) , without knowing how many nodes will have in advance, and by O(1) running time.

## the main class:
For this I implemented the abstract class:
* GraphInterface - implemented by class [DiGraph](https://github.com/hila-wiesel/OOP--ex3/wiki/DiGraph)
* Inside DiGraph class I implemented also an inner class [Node](https://github.com/hila-wiesel/OOP--ex3/wiki/Node)
* GraphAlgoInterface - implemented by class [GraphAlgo](https://github.com/hila-wiesel/OOP--ex3/wiki/GraphAlgo)

## Wiki page:
 https://github.com/hila-wiesel/OOP--ex3/wiki.
 
 There you can see deeper explantions about the project, and comperations of running-time of this project to others.




(c) Hila Wiesel
