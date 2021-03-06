from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pandas as pd
import edward as ed
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import networkx as nx

from edward.models import Normal, Poisson, InverseGamma
#from observations import celegans
import collections

X = pd.read_csv("/user_network.csv") #
X.columns = ['id','unix_time', 'dst_id',"src_id"]

X.iloc[:, 2:4].to_csv("/network_10k.edgelist",sep = " " ,index = False)

G = nx.read_edgelist("/network_excluded.edgelist",create_using=nx.DiGraph()) # read and parse edgelist to (networkx) graph
A = nx.adjacency_matrix(G) # make Adjacency matrix
x_train = np.asarray(A.todense()) # convert Adjacency matrix to numpy array
