#locus_name=input()

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import sys

locus_name = sys.argv[1]


print ("Blasting...")
#result_handle = NCBIWWW.qblast("blastp", "env_nr", locus_name , hitlist_size=200)
#with open("blastp_log.xml", "w") as out_handle:
#    out_handle.write(result_handle.read())
#result_handle.close()
result_handle = open("blastp_log.xml")


print ("Parsing...")
blast_record = NCBIXML.read(result_handle)

IDENTITY_VALUE = 0.3
E_VALUE_THRESH = 0.04

count = 0
f1 = open(f"blast_result_for_{locus_name}.log", 'w')
f1.write(f"****Alignment {locus_name}**** \n")
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        IDENTITY = (hsp.identities/hsp.align_length)
        if IDENTITY >= IDENTITY_VALUE and hsp.expect < E_VALUE_THRESH:
            f1.write(f"sequence: {alignment.title} \n")             
            f1.write(f"coverage: {str(hsp.align_length/alignment.length)} \n")
            f1.write(f"identity: {str(hsp.identities/hsp.align_length)} \n")
            f1.write(f"e value: {str(hsp.expect)} \n")
            count+=1
f1.write(f"num_aligments: {count} \n")
f1.close()

fs1 = open(f"blast_result_for_{locus_name}.fa", 'w')
for alignment in blast_record.alignments:
            IDENTITY = (hsp.identities/hsp.align_length)
            IDENTITY_VALUE = 0.3
            for hsp in alignment.hsps:
                if IDENTITY >= IDENTITY_VALUE:               
                    fs1.write(">" + alignment.title +'\n')
                    fs1.write(hsp.sbjct + '\n')
fs1.close()
print ("Done!")

import cd_hit
cd_hit.cdhit_meta(f"blast_result_for_{locus_name}.fa",f"clusters_{locus_name}.fa", 0.7)



#if __name__ == "__main__":
#    main()
