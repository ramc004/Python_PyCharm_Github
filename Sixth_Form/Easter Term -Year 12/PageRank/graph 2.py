class node(object):
  '''This class describes a node, to be used in the digraph later. each node features inbound and outbound edges (representing links to and from other webpages being considered'''
  def __init__(self,inbound=None, outbound=None):
    self.name = ''


    if inbound:
      self.inbound = inbound
    else:
      self.inbound = []

    if outbound:
      self.outbound = outbound
    else:
      self.outbound = []

  #creates links to and from other sites involving the node
  def add_outbound_edge(self,node):
    self.outbound.append(node)
    node.inbound.append(self)

  def add_inbound_edge(self,node):
    node.outbound.append(self)
    self.inbound.append(node)



class graph(object):
  '''All nodes are used in a digraph (in this case each edge only travels one way between two nodes) this class contains a dictionary of node names, which themselves as a class contain relevant edges'''
  def __init__(self,nodes = None):
    if nodes:
      self.nodes = nodes
    else:
      self.nodes = {}
      
  def add_node(self,node_name,node):
    node.name = node_name
    self.nodes[node_name] = node

  def add_edge(self,start_node,end_node):
    start = self.nodes[start_node]
    end = self.nodes[end_node]
    start.add_outbound_edge(end)

  def get_neighbours(self,node_name):
    node=self.nodes[node_name]
    neighbours = node.outbound()
    return neighbours

  def remove_node(self,node_name):
    if node_name in self.graph:
      del self.nodes[node_name]
  #returns a list of node
  def get_nodes(self):
    nodes = list(self.nodes.values())
    return nodes

