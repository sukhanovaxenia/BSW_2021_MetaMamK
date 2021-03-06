if (!requireNamespace("BiocManager", quietly = TRUE))
  +     install.packages("BiocManager")
list.of.packages <- c('dplyr','ggplot2','ggtree','treeio','phytools')
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)

library(ape)
library(treeio)
library(ggtree)
library(phytools)
library(dplyr)
treefile=dir(pattern = '*fa.treefile')
taxfile=dir(pattern='^parsed.*?\\.txt')
pngfile='tree_plot.png'
tree <- read.tree(treefile)
tree_r<- midpoint.root(tree)
edge<-data.frame(tree_r$edge, edge_num=1:nrow(tree_r$edge))
colnames(edge)<-c('parent', 'node', 'edge_num')
taxonomy<-read.table(taxfile, sep='|', header=F)
colnames(taxonomy)<-c('Accession', 'Protein', 'Lineage', 'Ecology')
taxonomy2<-filter(taxonomy, Accession %in% tree_r$tip.label)
tree_r$tip.label<-taxonomy2$Ecology
#Load unique parents numbers into group:
group<-groupClade(tree_r, .node=c(min(edge$parent):max(edge$parent)))
png(filename=pngfile)
ggtree(group, aes(color=group), rooted=TRUE)+geom_tiplab(size=1.8)+theme(legend.position='none')
dev.off()

