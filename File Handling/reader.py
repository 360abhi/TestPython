import os
import shutil

with open('File Handling/demo.txt',mode='r') as file:
    # content = file.read()
    # print(content)
    for line in file:
        print(line.strip())

shutil.move('data.json','File Handling/copied.json')


# with open('File Handling/demo.txt',mode='a') as file:
    # file.write("\n Hi im here also")