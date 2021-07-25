#!/usr/bin/env python
# coding: utf-8

# In[1]:

import sys
import os
import apt

cache = apt.Cache()
if cache['cd-hit'].is_installed:
    print "YES it's installed"
else:
    print "NO it's NOT installed"
    os.system(f'sudo apt-get install cd-hit')
 
db=sys.argv[1]
out=sys.argv[2]

def cdhit_meta(db,out):
    
    # pipeline.py input.fasta  out.fa

    #db='/mnt/c/Users/sukha/mamK_all_org_v8.fa'
    #out='/mnt/c/Users/sukha/mamK_cd_hit'
    os.system(f'cd-hit -i {db} -c 0.7 -o {out}')

cdhit_meta(db,out)

if __name__ == "__main__":
    main()
