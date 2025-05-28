import pandas as pd
import os
import sys

# curr_dir = os.path.dirname(os.path.abspath(__file__))
# root_path = os.path.abspath(os.path.join(curr_dir,'..','..'))
# sys.path.append(root_path)


    
def getData(filepath:str,sheetname:str):
    df = pd.read_excel(filepath,sheet_name=sheetname,engine='odf')
    return df