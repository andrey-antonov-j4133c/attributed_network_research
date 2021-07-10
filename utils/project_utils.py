import os

import networkx as nx
import numpy as np
from scipy.sparse import csr_matrix

def preprocess_polit_blogs(gml, raw_path):
  """
  creates a .npz formated dataset from GML
  """
  G = nx.read_gml(gml)
  sparce_matrix = nx.convert_matrix.to_scipy_sparse_matrix(G)

  attributes = nx.get_node_attributes(G, 'value')

  attributes = [int(itm) for itm in attributes.values()]
  attr_matrix = csr_matrix([0,1])

  np.savez(
      raw_path,

      adj_data=sparce_matrix.data, 
      adj_indices=sparce_matrix.indices, 
      adj_indptr=sparce_matrix.indptr,
      adj_shape=sparce_matrix.shape,

      attr_data=attr_matrix.data, 
      attr_indices=attr_matrix.indices, 
      attr_indptr=attr_matrix.indptr,
      attr_shape=attr_matrix.shape,

      labels=attributes
      )


def prepare_magfit_input_data(dataset_name, path, G, number_of_attributes):
  dir = f'{path}{dataset_name}/'
  create_dir(dir)

  conf_path = dir + 'inti.config'
  graph_path = dir + 'graph.txt'

  conf_line = '0.4 & 0.8 0.4;0.4 0.2\n'

  conf_file = open(conf_path, 'w')
  for _ in range(number_of_attributes):
    conf_file.write(conf_line)
  conf_file.close()

  nx.readwrite.edgelist.write_edgelist(G, graph_path, data=False)
  

def prepare_mag_result_file(path, dataset):
  dir = f'{path}{dataset}/'
  create_dir(dir)
  fname = dir + dataset + '.txt'
  #f = open(fname, 'w')
  #f.close()
  return fname

def get_mag_result_file(path, dataset):
  dir = f'{path}{dataset}/'
  fname = dir + dataset + '.txt'
  return fname


def open_npz(path):
  data = np.load(path)

  return {
    'adj_data': data['adj_data'],
    'adj_indices': data['adj_indices'],
    'adj_indptr': data['adj_indptr'],
    'attr_data': data['attr_data'],
    'attr_indices': data['attr_indices'],
    'attr_indptr': data['attr_indptr'],
    'attr_shape': data['attr_shape'],
    'labels': data['labels']
  }

def create_dir(path):
  try:
    os.makedirs(path)
  except OSError:
      print ("Creation of the directory %s failed" % path)
  else:
      print ("Successfully created the directory %s " % path)


def save_graph(G, dir, filename):
  create_dir(dir)
  nx.write_adjlist(G, dir+filename)

def save_fetures(features, dir, filename):
  create_dir(dir)
  f = open(dir+filename, "w")

  for row in features:
    row_str = ','.join([str(itm) for itm in row])
    f.write(f'{row_str}\n')
    
  f.close()
  
def save_mag_fetures(features, dir, filename):
  create_dir(dir)
  f = open(dir+filename, "w")

  for row in features:
    row_str = ','.join([itm for itm in row.split(' ')[:len(row.split(' '))-1]])
    f.write(f'{row_str}\n')
    
  f.close()
