import os
import sys
import pytest

curr_dir = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(curr_dir,'..','..'))
sys.path.append(root)

from Selenium.Scripts import Runner as run
from concurrent.futures import ThreadPoolExecutor

Sheetnames = ["Sheet1","Sheet2","Sheet3"]
mydf = []

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(run.execute, Sheetnames)

    for result in results:
        print(f"Result :{result}")

@pytest.mark.parametrize("sheetname",[('Sheet1'),('Sheet2'),('Sheet3')])
def test_all(sheetname):
    run.execute(sheet_name=sheetname)

