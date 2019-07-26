# Note this assumes undirected and unweighted right now TMC

import sys
import networkx
import random
random.seed(1234)

class Tab2GMLPlugin:
   def input(self, file):
      tabfile = open(file, 'r')
      nodes = ()#set()
      edges = ()#set()

      for line in tabfile:
         elements = line.split("\t")
         node1 = elements[0].strip()
         node2 = elements[1].strip()
         if (node1 not in nodes):
            nodes += (node1,)
         if (node2 not in nodes):
            nodes += (node2,)
         edge = (node1, node2)
         if (edge not in edges):
            edges += (edge,)

      self.G = networkx.OrderedGraph()
      self.G.add_nodes_from(nodes)
      self.G.add_edges_from(edges)
      #for node in nodes:
      #   self.G.add_node(node)

      #for edge in edges:
      #   self.G.add_edge(edge[0], edge[1], weight=0.5)
      #   self.G.add_edge(edge[1], edge[0], weight=0.5)

   def run(self):
      pass

   def output(self, file):
      #gmlfile = open(file, 'w')

      networkx.write_gml(self.G, file)

 

