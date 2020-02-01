import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

def draw_graph(nodes = [], edges = [], node_descriptions = {}):

    G = nx.DiGraph()
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap = plt.get_cmap('jet'), node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist = edges)
    plt.show()
