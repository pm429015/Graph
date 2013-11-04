.. -*- mode: rst -*-

About
=====

Graph algorithms for python



How to use ?
==============

Declare an object Btree or BST::

    graph = Graph()
    
Add new edge ( v1, v2, weight) ::

    graph.edgeAdd(v1, v2, weight)

print graph (start point) ::

    graph.DFS(start)
    graph.BFS(start)
    
Kruskal algorithm ::
    
    graph.Kruskal()
    
Prom algorithm::
    
    graph.Prim()
    
    
