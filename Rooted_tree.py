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

tree <- read.tree(sprintf('al_clusters_%s.fa.treefile', locus_name))
tree_r<- midpoint.root(tree)
edge<-data.frame(tree_r$edge, edge_num=1:nrow(tree_r$edge))
colnames(edge)<-c('parent', 'node', 'edge_num')
taxonomy<-read.table('tax.txt', sep='|', header=F)
colnames(taxonomy)<-c('Accession', 'Protein', 'Lineage', 'Ecology')
taxonomy2<-filter(taxonomy, Accession %in% tree_r$tip.label)
tree_r$tip.label<-taxonomy2$Ecology
#Load unique parents numbers into group:
group<-groupClade(tree_r, .node=c(min(edge$parent):max(edge$parent)))
png(filename='tree.png')
ggtree(group, aes(color=group), rooted=TRUE)+geom_tiplab(size=1.8)+theme(legend.position='none')
dev.off()
