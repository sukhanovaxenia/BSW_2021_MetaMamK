#!/usr/bin/env python
# coding: utf-8

# In[50]:


get_ipython().run_line_magic('load_ext', 'rpy2.ipython')

%%R
if (!requireNamespace("BiocManager", quietly = TRUE))
  +     install.packages("BiocManager")
BiocManager::install("treeio")
BiocManager::install("ggtree")
BiocManager::install("phytools")
library("treeio")
library("ggtree")
library("phytools")

tree <- read.tree(file=('C:/Users/Professional/documents/al_clusters_VAW75462.1.fa.treefile'))
edge<-data.frame(tree$edge, edge_num=1:nrow(tree$edge))
colnames(edge)<-c('parent', 'node', 'edge_num')
tree <- root(tree, outgroup=1, resolve.root=TRUE)
tree<- midpoint.root(tree)

group<-groupClade(tree, .node=c(58:112))
ggtree(group, aes(color=group), rooted=TRUE)+geom_tiplab()
