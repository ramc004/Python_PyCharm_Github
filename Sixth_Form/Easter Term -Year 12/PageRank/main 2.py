from graph import node,graph
from pagerank import pagerank

a = node()
b = node()
c = node()

g = graph()

g.add_node('A',a)
g.add_node('B',b)
g.add_node('C',c)

g.add_edge('A','B')
g.add_edge('B','C')
g.add_edge('A','C')
g.add_edge('C','A')


ranks = pagerank(g)

for node,value in ranks.items():
  print(node.name,value)