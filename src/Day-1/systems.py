import os
import sys

dir_name = os.path.abspath("../PYTHON/")
python_list = []
totalLines = 0

try:
    for root,_,files in os.walk(dir_name):
        for file in files:
            if file.endswith('.py'):
                filename = os.path.join(root,file)
                with open(file=filename,mode='r') as read:
                    totalLines += len(read.readlines())
                python_list.append(filename)
except Exception as r:
    print(str(r))


print(python_list)
print(totalLines)