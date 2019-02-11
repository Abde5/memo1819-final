import networkx as nx
import matplotlib.pyplot as plt
import numpy

_classes = nx.DiGraph()
_classes.add_node("coco")
_classes.add_node("TSG")
_classes.add_node("MUIG")
_classes.add_node("UUIG")
_classes.add_node("TTLG")
_classes.add_node("IG")
_classes.add_node("UIG")
_classes.add_node("UDG")

# inclusions

_edges = {
    ('TSG','coco'):'[1]',
    ('UUIG','coco'):'[2]',
    ('TSG','UUIG'):'[3]',
    ('TSG','UDG'):'[4]',
    ('MUIG','TSG'):'[5]',
    ('UIG','IG'):'[6]',
    ('UIG','MUIG'):'[7]',
    ('UIG','TTLG'):'[8]'

    }

_classes.add_edge("TSG","coco")
_classes.add_edge("UUIG","coco")
_classes.add_edge("TSG","UUIG")
_classes.add_edge("TSG","UDG")
_classes.add_edge("MUIG","TSG")
_classes.add_edge("UIG","IG")
_classes.add_edge("UIG","MUIG")
_classes.add_edge("UIG","TTLG")
_classes.add_edge("MUIG","IG")
_classes.add_edge("IG","coco")
_classes.add_edge("TTLG","TSG")


#show

options = {
    'node_color': 'white',
    'node_size': 2000,
    #'width': 3,
    'with_labels': True,
    'node_shape': 's'
}

# layout

pos = nx.nx_pydot.graphviz_layout(_classes,prog='dot')

nx.draw(_classes,pos, **options)
nodes = nx.draw_networkx_nodes(_classes, pos, **options)
nodes.set_edgecolor('#000000')
nx.draw_networkx_edge_labels(_classes,pos,edge_labels=_edges, **options)
plt.axis('off')
plt.show()
