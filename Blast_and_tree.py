from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import sys
import os

locus_name = sys.argv[1]


print ("Blasting...")
if not os.path.isfile("blastp_log.xml"):
    
    result_handle1 = NCBIWWW.qblast("blastp", "env_nr", locus_name , hitlist_size=200)
    result_handle2 = NCBIWWW.qblast("blastp", "nr", locus_name , hitlist_size=200)

    with open("blastp_log.xml", "w") as out_handle:
        out_handle.write(result_handle1.read())
    with open("blastp_log.xml", "a") as out_handle:
        out_handle.write(result_handle2.read())   

    result_handle1.close()
    result_handle2.close()

result_handle = open("blastp_log.xml",'r')


print ("Parsing...")
blast_records = NCBIXML.parse(result_handle)

IDENTITY_VALUE = 0.3
E_VALUE_THRESH = 0.04

count = 0
f1 = open(f"blast_result_for_{locus_name}.log", 'w')
f1.write(f"****Alignment {locus_name}**** \n")

accessions = open(f"accessions_{locus_name}.txt", 'w')
for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            IDENTITY = (hsp.identities/hsp.align_length)
            if IDENTITY >= IDENTITY_VALUE and hsp.expect < E_VALUE_THRESH:
#                print(alignment.title.split("|")[1])
                accessions.write(alignment.title.split("|")[1] + "\n")             
#                print(hsp.query)
                f1.write(f"sequence: {alignment.title} \n")             
                f1.write(f"coverage: {str(hsp.align_length/alignment.length)} \n")
                f1.write(f"identity: {str(hsp.identities/hsp.align_length)} \n")
                f1.write(f"e value: {str(hsp.expect)} \n")
                count+=1
f1.write(f"num_aligments: {count} \n")
f1.close()
accessions.close()

fs1 = open(f"blast_result_for_{locus_name}.fa", 'w')
for blast_record in blast_records:  
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            IDENTITY = (hsp.identities/hsp.align_length)
            if IDENTITY >= IDENTITY_VALUE and hsp.expect < E_VALUE_THRESH:              
                    fs1.write(">" + alignment.title.split("|")[1] +'\n')
                    fs1.write(hsp.sbjct.replace("-","") + '\n')
fs1.close()
print ("Done!")

import cd_hit
cd_hit.cdhit_meta(f"blast_result_for_{locus_name}.fa",f"clusters_{locus_name}.fa", 0.7)
import Build_tree
Build_tree.tree(f"clusters_{locus_name}.fa")



#if __name__ == "__main__":
#    main()
