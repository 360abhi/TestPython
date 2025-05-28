import os
import sys

curr_dir = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(curr_dir,'..','..'))
sys.path.append(root)

from Selenium.Scripts import Runner as run

# Sheetnames = ["Sheet1","Sheet2","Sheet3"]

run.execute(sheet_name="Sheet1")