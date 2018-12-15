# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:43:14 2018

@author: paubc
"""

class Graph:
    
    def __init__(self):
        self._nodes={}
        self._edges={}
        
    
    @property
    def node(self):
        return self._nodes
    
    @property
    def edge(self):
        return self._edges
    
    def nodes(self):
        _list_nodes=[]
        for i in self.node.keys():
            _list_nodes.append(i)
        return _list_nodes
        
        
    
    def edges(self):
        _list_edges=[]
        for i,edges in self._edges.items():
            for j in edges.keys():
                
                if (i<=j):
                    nova_aresta=(i,j)
                else:
                    nova_aresta=(j,i)
                
            if nova_aresta not in _list_edges:
                _list_edges.append(nova_aresta)
        return _list_edges
            
            
            
        
    
    def add_node(self, node, attr_dict=None):
        atributs={}
        
        if attr_dict!=None:

            atributs=attr_dict
        
        self._nodes[node]=atributs
        
        
        
        
    
    def add_edge(self, node1, node2, attr_dict=None):
        if node1 not in self._nodes.keys():
            self.add_node(node1)
        if node2 not in self._nodes.keys():
            self.add_node(node2)
        
        if attr_dict!=None:

            self._edges.setdefault(node1,{})[node2]=attr_dict
            self._edges.setdefault(node2,{})[node1]=attr_dict
        else:
            self._edges.setdefault(node1,{})[node2]={}
            self._edges.setdefault(node2,{})[node1]={}
            

            
        
    def add_nodes_from(self, node_list, attr_dict=None):
        for i in node_list:
            self.add_node(i,attr_dict)
    
    def add_edges_from(self, edge_list, attr_dict=None):
        for i in edge_list:
            self.add_edge(i[0],i[1],attr_dict)
            
            
            
            
    
    
    def degree(self,node):
        return len(self._edges.get(node).items())
        
        
            
    
    def __getitem__(self, node):
        
        adyacentes={}
        
        for i in self.neighbors(node):
            adyacentes[i]=self._edges[node][i]
            
        return adyacentes
            
        
    
    def __len__(self):
        return len(self._nodes)
    
    def neighbors(self, node):
        listavecinos=[]
        for i in self._edges.get(node).keys():
            listavecinos.append(i)
        return listavecinos
            

    def remove_node(self, node1):
        
        self._nodes.pop(node1)
        self._edges.pop(node1)
        
        for i,edges in self._edges.items():
            for k in list(edges.keys()):
                if k==node1:
                    edges.pop(k)
            
                
        
    
    def remove_edge(self, node1, node2):
        for i,edges in list(self._edges.items()):
            if i==node1:
                for k in list(edges.keys()):
                    if k==node2:
                        edges.pop(node2)
            elif i==node2:
                for n in list(edges.keys()):
                    if n==node1:
                        edges.pop(node1)
                

                    
        
                
    
    def remove_nodes_from(self, node_list):
        for i in node_list:
            self.remove_node(i)
    
    def remove_edges_from(self, edge_list):
        for i in edge_list:
            self.remove_edge(i[1],i[0])