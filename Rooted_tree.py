#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'rpy2.ipython')

# In[2]:


%%R -i locus_name 
if (!requireNamespace("BiocManager", quietly = TRUE))
  +     install.packages("BiocManager")
BiocManager::install("treeio")
BiocManager::install("ggtree")
BiocManager::install("phytools")
library("treeio")
library("ggtree")
library("phytools")

tree <- read.tree(file=sprintf('al_clusters_%s.fa.treefile', locus_name))
edge<-data.frame(tree$edge, edge_num=1:nrow(tree$edge))
colnames(edge)<-c('parent', 'node', 'edge_num')
tree <- root(tree, outgroup=1, resolve.root=TRUE)
tree<- midpoint.root(tree)

group<-groupClade(tree, .node=c(min(edge$parent):max(edge$parent)))
ggtree(group, aes(color=group), rooted=TRUE)+geom_tiplab(size=1.5)+theme(legend.position='none')
