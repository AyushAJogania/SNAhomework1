# SNAhomework1

Diameter of Random Graph Problem 
This repository contains Python code to solve the diameter of a random graph problem using BFS (breadth-first search) algorithm.

Problem Statement: 
The diameter of a graph is defined as the maximum distance between any pair of nodes in the graph. Given a random graph with n nodes and p probability of an edge between any two nodes, the problem is to find the diameter of the graph.

The code is an implementation of the BFS algorithm to find the diameter of a random graph.

First, the find_diameter function takes two inputs, n which is the number of nodes in the graph, and p which is the probability of edge creation between any two nodes.

Next, a dictionary named graph is created with nodes as keys and an empty list as values. A for loop is used to iterate through each node and another nested for loop is used to randomly determine if an edge exists between two nodes. If the probability p is greater than a random value generated using random.random(), then an edge is created between the nodes by appending the other node to the list of connected nodes of that node in the graph dictionary.

After creating the graph, the bfs function is defined. It takes two inputs, node and parent. It performs the BFS algorithm and returns the distance from the node to the farthest node. It starts by initializing a queue with a tuple containing the node and distance as 0. A set called visited is created to keep track of visited nodes, a variable farthest_node is set to the node and farthest_distance is set to 0. A while loop is used to iterate over the queue until it is empty. The current node and its distance from the starting node are retrieved from the front of the queue using pop(0). The node is added to the visited set and if the distance is greater than the farthest_distance, then the farthest_distance is updated with the current distance and farthest_node is updated with the current node. The for loop iterates over the connected nodes of the current node and if a neighbor is not in the visited set, then it is added to the queue with its distance from the starting node incremented by 1.

Finally, the find_diameter function is used to perform a BFS starting from each node and finding the farthest node from it. The farthest_node and its distance from the starting node are retrieved from the BFS algorithm. Another BFS is performed starting from the farthest_node to find the diameter of the graph. The diameter is returned from the function.

Finally, the diameter variable is printed using the print() function. It displays the diameter of the random graph created using the find_diameter function
