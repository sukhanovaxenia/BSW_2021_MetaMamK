import sys
import os
import apt

cache = apt.Cache()
if cache['mafft'].is_installed and cache['iqtree'].is_installed:
    print ("YES it's installed")
else:
    print ("NO it's NOT installed")
    os.system(f'sudo apt-get update -y')
    os.system(f'sudo apt-get install -y mafft')
    os.system(f'sudo apt-get install -y iqtree')

def tree(infile):
    os.system(f"mafft {infile} > al_{infile}")
    os.system(f"fasttree {infile} > fatree.tree")

def main():
    db=sys.argv[1]
    #out=sys.argv[2]

    tree(db)

# pipeline.py input.fasta

#input_file = sys.argv[1]
