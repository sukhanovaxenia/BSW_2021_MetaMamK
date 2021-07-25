# BSW_2021_MetaMamK
This repository includes generated script for search protein homologues of targeted enzymes'. The research is based on MamK protein of magnetotactic bacteria. 

Goal:
Provide a tool for automated search for bacterial enzymes which are homologues for the targeted ones.

Scripts description:

Blast_and_tree.py - the main united function for blasting on the protein sequence, clustering homologues and building .nwk tree based on the alignment.
1. Blast furnction generates .fa alignment, .log file with identity, e-value and hits, .txt file with accession numbers; chosen number of sequences is 200 to cut-off hardly homological proteins
2.cd_hit.py - function for clustering homologues, the threshold is default = 0.9; input  - blast output; output - two file: .fa with centroids fasta, .clstr with clusters' contain
3.Build_tree.py - function for building .nwk tree.; input - centroids' .fa file; output - .treefile format tree (this format contains .nwk tree information)
4.Taxonomy_parse - function for taxonomy export form NCBI database, the chosen category is 'Lineage'; input - the accession .txt file generated on the first step (blasr analysis)
5. Rooted_tree.py - function for tree visualization with R language packages ('phyltools', 'ape','treeiop','ggtree'); the output tree is rooted and coloured by parent's nodes. This tree-visualizetion script is manual as necessary nodes' numbers are not common.
