# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:47:00 2020

@author: HP
"""

from Bio.PDB import PDBList
import pandas as pd

pdbl = PDBList()
filname = 'PDB_Codes'
data = pd.read_csv(r'C:\Users\HP\Desktop\Research Assistant\DNA Project\PDB_Codes.csv', low_memory=False)
PDBlist_BDNA=data.BDNA.tolist()
print(PDBlist_BDNA)
for i in PDBlist_BDNA:
    pdbl.retrieve_pdb_file(i,pdir='PDB')
    
print('BDNA done!')