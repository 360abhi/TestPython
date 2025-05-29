import json

sample = {"keya":"valuea","keyb":"valueb","keyc":30}
with open('data.json', mode='w') as file:
    json.dump(sample,file,indent=4)