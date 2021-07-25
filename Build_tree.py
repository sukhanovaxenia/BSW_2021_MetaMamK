import sys
import os
db=sys.argv[1]
out=sys.argv[2]

def cdhit_meta(db,out):
    
    # pipeline.py input.fasta  out.fa

    #db='/mnt/c/Users/sukha/mamK_all_org_v8.fa'
    #out='/mnt/c/Users/sukha/mamK_cd_hit'
    os.system(f'cd-hit -i {db} -c 0.7 -o {out}')
    os.system(f"mafft {out} > al_{out}")
    os.system(f"iqtree -s al_{out} -m TEST -bb 1000 -nt 4")
cdhit_meta(db,out)

# pipeline.py input.fasta

#input_file = sys.argv[1]
