import pandas as pd

def getData(filepath:str,sheetname:str):
    df = pd.read_excel(filepath,sheet_name=sheetname,engine='odf')
    return df