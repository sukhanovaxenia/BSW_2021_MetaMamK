#!/usr/bin/env python
# coding: utf-8

# In[75]:


import Bio
from Bio import Entrez
import sys
Entrez.email='sukhanovaxenia@gmail.com'


def tax_parse(inl,outtax):
    inlist=[]
    with open(inl, 'r') as f:
        for line in f:
            inlist.append(line.strip())
    inlist_str = ",".join(inlist)
    handle = Entrez.efetch(db="protein", id=inlist_str, retmode="xml")
    records = Entrez.read(handle)
    handle.close()
    count = 0
    with open(outtax, "w") as outfile:
        for i in  records:
            print (inlist[count], i["GBSeq_definition"], i["GBSeq_taxonomy"], i['GBSeq_source'])
            outfile.write(f'{inlist[count]} | {i["GBSeq_definition"]} | {i["GBSeq_taxonomy"]} | {i["GBSeq_source"]} \n')
            count+=1
    
#    handle = Entrez.esearch(db="protein", term ="MBA7623740.1", retmax=100500)
   # except RuntimeError(value):
    #    print("Invalid id")
 
def main():
    inl=sys.argv[1]
    outtax=sys.argv[2]
    tax_parse(inl, outtax)

if __name__ == "__main__":
    main()
        

    
    
        




