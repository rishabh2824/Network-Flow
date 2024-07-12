Complete implemention of the Ford-Fulkerson method for finding maximum flow in graphs with only integer edge capacities.
Deployed an efficient algorithm in O(mF) time, where m is the number of edges in the graph and F is the value of the maximum flow in the graph.
The input starts with a positive integer, giving the number of instances that follow. 
For each instance, there will be two positive integers, indicating the number of nodes n = |V| in the graph and the number
of edges m = |E| in the graph. Following this, there will be |E| additional lines describing the edges.
Each edge line consists of a number indicating the source node, a number indicating the destination node, and a capacity c(e). 
The nodes are not listed separately, but are numbered {1 . . . n}.
The program omputes the maximum flow value from node 1 to node n in each given graph.
