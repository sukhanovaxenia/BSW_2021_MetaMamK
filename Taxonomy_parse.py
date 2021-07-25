#!/usr/bin/env python
# coding: utf-8

# In[75]:


import Bio
from Bio import Entrez
import sys

inl=sys.argwv[1]
outtax=sys.argv[2]

def tax_parse(inl,outtax):
    inlist = inl
    handle = Entrez.esummary(db="protein", id = ','.join(inlist), retmax=100500)
    entry=Entrez.read(handle)
    tax_id=entry[0]
    ids=[]
    for elem in entry:
        ids.append(str(elem['TaxId']))
    ids_str=','.join(ids)
    tax=Entrez.efetch(db='Taxonomy', id=ids_str, retmax=100500, retmode  = "xml")
    tax1=Entrez.read(tax)
    taxonomy=[]
    for elem1 in tax1:
        taxonomy.append(str(elem1['Lineage']))
    with open(outtax, 'w') as output:
        for i in range(0,len(inlist)):
            output.write(print(inlist[i], taxonomy[i]))
 
tax_parse(inl, outtax)

if __name__ == "__main__":
    main()
    
    
    
        




